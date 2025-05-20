import os
import sys
import time
import json
import logging
import pandas as pd
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from sklearn.preprocessing import StandardScaler
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.connection_db import create_tables, load_data

TOPIC = os.getenv("TOPIC", "happiness_data")
BROKER = os.getenv("BROKER", "localhost:29092")
GROUP_ID = os.getenv("GROUP_ID", "happiness_group")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 50))
MODEL_PATH = os.getenv("MODEL_PATH", "./model/model.pkl")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

model = joblib.load(MODEL_PATH)

def preprocess_message(record):
    """
    Convierte un mensaje de Kafka en un DataFrame preparado para predicciones.
    """
    try:
        df = pd.DataFrame([record])

        feature_columns = [
            'year', 'gdp_per_capita', 'social_support', 'healthy_life_expectancy',
            'freedom', 'corruption', 'generosity', 'america', 'asia', 'central_america',
            'europe', 'north_america', 'oceania', 'south_america'
        ]


        for col in feature_columns:
            if col not in df.columns:
                df[col] = 0

        df = df[feature_columns + ['happiness_score']]if 'happiness_score' in df.columns else df[feature_columns]
        
        df['predicted_happiness_score'] = model.predict(df[feature_columns])

        if (df['predicted_happiness_score'] < 0).any() or (df['predicted_happiness_score'] > 10).any():
            raise ValueError("Predicted happiness score out of expected range (0-10)")
        
        return df
    
    except Exception as e:
        logger.error(f"Error en la preparación del mensaje: {e}")
        return None


def kafka_consumer():
    """
    Consume mensajes de Kafka, los procesa y los guarda en la base de datos.
    """
    try:
        consumer = KafkaConsumer(
            TOPIC,
            bootstrap_servers=[BROKER],
            group_id=GROUP_ID,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            consumer_timeout_ms=5000
        )

        logger.info("Conexión exitosa a Kafka.")

        batch = []
        while True:
            try:
                for message in consumer:
                    record = preprocess_message(message.value)
                    
                    if record is not None:
                        batch.append(record)

                    if len(batch) >= BATCH_SIZE:
                        for row in batch:
                            load_data(row.to_dict(orient="records")[0])
                        logger.info(f"Procesados {len(batch)} registros.")
                        batch = []

            except KafkaError as ke:
                logger.error(f"Error al consumir mensajes de Kafka: {ke}")
                time.sleep(5)

            if batch:
                for row in batch:
                    load_data(row.to_dict(orient="records")[0])
                logger.info(f"Procesados {len(batch)} registros finales.")
                batch = []

    except Exception as e:
        logger.error(f"Error inicializando el consumidor de Kafka: {e}")

    finally:
        try:
            consumer.close()
            logger.info("Conexión con Kafka cerrada.")
        except Exception as e:
            logger.error(f"Error cerrando el consumidor: {e}")


if __name__ == "__main__":
    create_tables()
    kafka_consumer()
