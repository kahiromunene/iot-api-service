import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "iot_db"),
        user=os.getenv("DB_USER", "iot_user"),
        password=os.getenv("DB_PASSWORD", "iot_pass"),
        cursor_factory=RealDictCursor
    )
