# app/core/models.py

def create_tables(conn):
    with conn.cursor() as cursor:
        cursor.execute(f"CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                shortened_url TEXT NOT NULL,
                hash TEXT NOT NULL UNIQUE,
                original_url TEXT NOT NULL
            );
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_hash ON urls (hash);")
        conn.commit()
