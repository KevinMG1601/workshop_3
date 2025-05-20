import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT", 3306),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )
        print("Successful connection to the database.")
        return conn
    except Exception as e:
        print(f"Database connection error:: {e}")
        return None

db_connection = None

def get_db_connection():
    global db_connection
    if db_connection is None or not db_connection.is_connected():
        db_connection = connection()
    return db_connection

def create_tables():
    conn = get_db_connection()

    if not conn:
        print("Could not connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS happiness_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            year INT,
            gdp_per_capita FLOAT,
            social_support FLOAT,
            healthy_life_expectancy FLOAT,
            freedom FLOAT,
            corruption FLOAT,
            generosity FLOAT,
            america BOOLEAN,
            asia BOOLEAN,
            europe BOOLEAN,
            oceania BOOLEAN,
            central_america BOOLEAN,
            north_america BOOLEAN,
            south_america BOOLEAN,
            happiness_score FLOAT,
            predicted_happiness_score FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()
        print("Table 'happiness_data' successfully created.")

    except Exception as e:
        print(f"Error creating the tables: {e}")
    finally:
        cursor.close()
        conn.close()

def load_data(row: dict):
    conn = get_db_connection()

    if not conn:
        print("Could not connect to the database to load data.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO happiness_data (year, gdp_per_capita, social_support, healthy_life_expectancy, freedom, corruption, generosity, 
            america, asia, europe, oceania, central_america, north_america, south_america, happiness_score, predicted_happiness_score)
        VALUES (%(year)s, %(gdp_per_capita)s, %(social_support)s, %(healthy_life_expectancy)s, %(freedom)s, %(corruption)s, %(generosity)s,
            %(america)s, %(asia)s, %(europe)s, %(oceania)s, %(central_america)s, %(north_america)s, %(south_america)s, %(happiness_score)s, %(predicted_happiness_score)s);
        """, row)   
        conn.commit()
        print("Data loading.")
    except Exception as e:
        print(f"Error loading data: {e}")
    finally:
        cursor.close()

def get_data():
    conn = connection()
    if not conn:
        print("Could not connect to the database to obtain data.")
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM happiness_data")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])
        cursor.close()
        conn.close()
        print("Data obtained")
        return df
    except Exception as e:
        print(f"Error obtaining data: {e}")
        return []


if __name__ == "__main__":
    create_tables()
