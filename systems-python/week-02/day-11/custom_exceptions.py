# Define the hierarchy
class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

class ConnectionTimeoutError(DatabaseError):
    def __init__(self, host, timeout_seconds):
        self.host = host
        self.timeout_seconds = timeout_seconds
        super().__init__(f"Connection to {host} timed out after {timeout_seconds}s")

# Simulate a database connection
def connect_to_database(host):
    print(f"Connecting to {host}...")
    raise ConnectionTimeoutError(host, 5)

# Catch it
try:
    connect_to_database("db.production.com")
except ConnectionTimeoutError as e:
    print(f"Timeout: {e.host} didn't respond in {e.timeout_seconds}s")
except DatabaseError as e:
    print(f"Database problem: {e}")
except AppError as e:
    print(f"App error: {e}")