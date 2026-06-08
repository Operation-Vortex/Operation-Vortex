import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
    )

# Test connection
conn = get_connection()
print("Connected to PostgreSQL successfully")
conn.close()
print("Connection closed")


import time

# Measure cost of creating new connections each time
print("\n--- 100 new connections (no pool) ---")
start = time.time()
for i in range(100):
    conn = get_connection()
    conn.close()
end = time.time()
print(f"100 new connections: {end - start:.4f} seconds")

# Measure cost with connection pool
from psycopg2 import pool

print("\n--- 100 queries with connection pool ---")
connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
)

start = time.time()
for i in range(100):
    conn = connection_pool.getconn()
    connection_pool.putconn(conn)
end = time.time()
print(f"100 pooled connections: {end - start:.4f} seconds")

connection_pool.closeall()


print("\n--- Pool exhaustion ---")
small_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=3,
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
)

connections = []
try:
    for i in range(5):
        conn = small_pool.getconn()
        connections.append(conn)
        print(f"Got connection {i+1}")
except Exception as e:
    print(f"Pool exhausted: {e}")
finally:
    for conn in connections:
        small_pool.putconn(conn)
    small_pool.closeall()
    print("All connections returned to pool")