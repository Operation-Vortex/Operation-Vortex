import sqlite3

# Fresh database
connection = sqlite3.connect("cutabove.db")
cursor = connection.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS barbers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY,
        barber_id INTEGER,
        client_name TEXT,
        appointment_time TEXT,
        FOREIGN KEY (barber_id) REFERENCES barbers(id)
    )
""")

# Insert only if empty
cursor.execute("SELECT COUNT(*) FROM barbers")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO barbers (name, phone) VALUES (?, ?)",
        [
            ("Kwame", "0241234567"),
            ("Kofi", "0559876543"),
            ("Ama", "0201234567"),
            ("Yaw", "0271234567"),
        ]
    )

    cursor.executemany(
        "INSERT INTO appointments (barber_id, client_name, appointment_time) VALUES (?, ?, ?)",
        [
            (1, "Emmanuel", "09:00"),
            (1, "Kojo", "10:00"),
            (2, "Abena", "09:30"),
            (3, "Fiifi", "11:00"),
        ]
    )
    connection.commit()
    print("Data inserted")

# INNER JOIN
print("\n--- INNER JOIN ---")
cursor.execute("""
    SELECT barbers.name, appointments.client_name, appointments.appointment_time
    FROM barbers
    INNER JOIN appointments ON barbers.id = appointments.barber_id
""")
for row in cursor.fetchall():
    print(row)

# LEFT JOIN
print("\n--- LEFT JOIN ---")
cursor.execute("""
    SELECT barbers.name, appointments.client_name, appointments.appointment_time
    FROM barbers
    LEFT JOIN appointments ON barbers.id = appointments.barber_id
""")
for row in cursor.fetchall():
    print(row)

# COUNT appointments per barber
print("\n--- Appointments per barber ---")
cursor.execute("""
    SELECT barbers.name, COUNT(appointments.id) as appointment_count
    FROM barbers
    LEFT JOIN appointments ON barbers.id = appointments.barber_id
    GROUP BY barbers.id
""")
for row in cursor.fetchall():
    print(row)

connection.close()