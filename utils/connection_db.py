import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def connection():
    """Create a connection to the database using SQLAlchemy.
    
    parameters:
        None
    returns:
        engine: SQLAlchemy engine object
        session: SQLAlchemy session object
    """     
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    database = os.getenv('DATABASE')

    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(url)
    return engine

if __name__ == "__main__":
    try:
        engine = connection()
        print("Conexión exitosa a la base de datos PostgreSQL")
    except Exception as e:
        print(f"Error de conexión: {e}")