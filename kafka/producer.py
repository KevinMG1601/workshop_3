import os
import sys
import time
import pandas as pd
from json import dumps
from kafka import KafkaProducer
from kafka.errors import KafkaConnectionError, KafkaTimeoutError
from sklearn.model_selection import train_test_split

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.training_functions import create_dummy

TOPIC = os.getenv("TOPIC", "happiness_data")
BROKER = os.getenv("BROKER", "localhost:29092")

rename = {
    'America': 'america',
    'Asia': 'asia',
    'Europe': 'europe',
    'Oceania': 'oceania',
    'Central America': 'central_america',
    'North America': 'north_america',
    'South America': 'south_america'
}

def load_data():
    """
    Carga los datos desde el archivo CSV y aplica las transformaciones necesarias.
    """
    df = pd.read_csv("./data/output/happiness_merged.csv")

    df_train, df_test = train_test_split(df, test_size=0.2, random_state=77)

    df_test = create_dummy(df_test)
    df_test = df_test.rename(columns=rename)
    df_test = df_test.drop(columns=["country"])

    return df_test

def produce_messages(df_test):
    """
    Envia los mensajes a Kafka en lotes.
    """
    try:
        producer = KafkaProducer(
            value_serializer=lambda m: dumps(m).encode('utf-8'),
            bootstrap_servers=[BROKER],
            batch_size=16384,
            linger_ms=10,
            api_version=(2, 6, 0),
            retries=5,
            request_timeout_ms=60000,
            max_block_ms=60000
        )
        print("Conectado a Kafka.")

        total_sent = 0
        batch_size = 50
        for start in range(0, len(df_test), batch_size):
            end = min(start + batch_size, len(df_test))
            batch = df_test.iloc[start:end].to_dict(orient='records')

            print("Primer mensaje del lote:", batch[0])

            for record in batch:
                try:
                    producer.send(TOPIC, value=record)
                    total_sent += 1
                except KafkaTimeoutError as e:
                    print(f"Error enviando mensaje: {e}")

            producer.flush()
            print(f"Enviado lote de {len(batch)} mensajes.")

        print(f"Todos los {total_sent} mensajes fueron enviados correctamente.")
        producer.close()

    except Exception as e:
        print(f"Error general en el productor: {e}")

if __name__ == '__main__':
    df_test = load_data()
    produce_messages(df_test)
