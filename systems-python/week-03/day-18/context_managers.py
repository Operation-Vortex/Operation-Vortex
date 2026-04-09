class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Opening connection to {self.db_name}")
        self.connection = f"conn_{self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"Success — committing changes to {self.db_name}")
        else:
            print(f"Error occurred — rolling back. Reason: {exc_val}")
        print(f"Closing connection to {self.db_name}")
        return False
    

    # Success path
print("--- Success path ---")
with DatabaseConnection("cutabove_db") as conn:
    print(f"Using {conn}")
    print("Executing query...")

# Failure path
print("\n--- Failure path ---")
with DatabaseConnection("cutabove_db") as conn:
    print(f"Using {conn}")
    raise Exception("Barber ID not found")