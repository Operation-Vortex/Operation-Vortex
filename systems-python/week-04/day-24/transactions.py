import sqlite3

# Setup
connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        balance REAL
    )
""")

# Only insert if empty
cursor.execute("SELECT COUNT(*) FROM accounts")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        [("Kwame", 1000), ("Kofi", 500)]
    )
    connection.commit()

# Show starting balances
cursor.execute("SELECT name, balance FROM accounts")
print("Starting balances:")
for row in cursor.fetchall():
    print(row)

connection.close()

print("\n--- Transfer WITHOUT transaction (dangerous) ---")
connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

try:
    # Step 1 — deduct from Kwame
    cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Kwame'")
    
    # Simulate a crash between the two operations
    raise Exception("Server crashed!")
    
    # Step 2 — add to Kofi (never runs)
    cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Kofi'")
    
    connection.commit()

except Exception as e:
    print(f"Error: {e}")
    connection.commit()  # accidentally commits the partial state

# Check balances after crash
cursor.execute("SELECT name, balance FROM accounts")
print("Balances after crash:")
for row in cursor.fetchall():
    print(row)

connection.close()


print("\n--- Transfer WITH transaction (safe) ---")

# Reset balances first
connection = sqlite3.connect("bank.db")
cursor = connection.cursor()
cursor.execute("UPDATE accounts SET balance = 1000 WHERE name = 'Kwame'")
cursor.execute("UPDATE accounts SET balance = 500 WHERE name = 'Kofi'")
connection.commit()

# Now do the transfer WITH a transaction
try:
    with connection:
        cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Kwame'")
        raise Exception("Server crashed again!")
        cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Kofi'")

except Exception as e:
    print(f"Error: {e}")

# Check balances
cursor.execute("SELECT name, balance FROM accounts")
print("Balances after crash WITH transaction:")
for row in cursor.fetchall():
    print(row)

connection.close()


print("\n--- Dirty read demonstration ---")

connection1 = sqlite3.connect("bank.db")
connection2 = sqlite3.connect("bank.db")

cursor1 = connection1.cursor()
cursor2 = connection2.cursor()

# Connection 1 makes a change but doesn't commit
cursor1.execute("UPDATE accounts SET balance = 9999 WHERE name = 'Kwame'")

# Connection 2 reads — what does it see?
cursor2.execute("SELECT name, balance FROM accounts WHERE name = 'Kwame'")
print(f"Connection 2 sees: {cursor2.fetchone()}")

# Connection 1 rolls back
connection1.rollback()

# Connection 2 reads again
cursor2.execute("SELECT name, balance FROM accounts WHERE name = 'Kwame'")
print(f"Connection 2 after rollback: {cursor2.fetchone()}")

connection1.close()
connection2.close()