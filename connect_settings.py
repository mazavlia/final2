import psycopg2
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
import sys
import os
# sys.path.insert(0, '/opt/airflow/dags/')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Connections settings

config = {
    'database': os.getenv("POSTGRES_DB"),
    'user': os.getenv("POSTGRES_USER_"),
    'password': os.getenv("POSTGRES_PASSWORD"),
    'host': os.getenv("POSTGRES_HOST"),
    'port': os.getenv("POSTGRES_PORT"),
}

engine = create_engine(f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:"
                       f"{config['port']}/{config['database']}")

conn = psycopg2.connect(**config)
