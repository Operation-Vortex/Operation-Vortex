import sqlite3
import time
import random

connection = sqlite3.connect("cutabove.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS barbers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        earnings REAL,
        active INTEGER
    )
""")

connection.commit()

# Insert 100,000 rows
names = ["Kwame", "Kofi", "Ama", "Yaw", "Abena", "Kojo", "Akua", "Fiifi"]

print("Inserting 100,000 rows...")
start = time.time()

for i in range(100000):
    name = random.choice(names)
    phone = f"024{random.randint(1000000, 9999999)}"
    earnings = round(random.uniform(0, 1000), 2)
    cursor.execute(
        "INSERT INTO barbers (name, phone, earnings, active) VALUES (?, ?, ?, ?)",
        (name, phone, earnings, 1)
    )

connection.commit()
print(f"Inserted in {time.time() - start:.4f} seconds")

# Query for a specific phone number - should be unique
print("\nQuerying for specific phone WITHOUT index...")
start = time.time()
cursor.execute("SELECT * FROM barbers WHERE phone = '0241234567'")
results = cursor.fetchall()
print(f"Found {len(results)} rows in {time.time() - start:.4f} seconds")

# Add index on phone
cursor.execute("CREATE INDEX IF NOT EXISTS idx_barber_phone ON barbers(phone)")
connection.commit()

print("\nQuerying for specific phone WITH index...")
start = time.time()
cursor.execute("SELECT * FROM barbers WHERE phone = '0241234567'")
results = cursor.fetchall()
print(f"Found {len(results)} rows in {time.time() - start:.4f} seconds")

connection.close()