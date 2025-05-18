# app/core/db.py

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.models import create_tables

DB_URL = os.getenv("DATABASE_URL") 

conn = None

def get_connection():
    global conn
    if conn is None or conn.closed:
        conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
    return conn

def init_db():
    connection = get_connection()
    if conn: print("connected to the db : ", DB_URL)
    create_tables(connection)

def execute_query(query, params=None, fetch_one=False, fetch_all=False):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        if fetch_one:
            return cursor.fetchone()
        if fetch_all:
            return cursor.fetchall()
        return None
