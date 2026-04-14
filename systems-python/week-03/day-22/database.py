import sqlite3

# Connect to a database file (creates it if it doesn't exist)
connection = sqlite3.connect("cutabove.db")

# A cursor is how you send instructions to the database
cursor = connection.cursor()

print("Database connected successfully")

connection.close()
print("Database closed")