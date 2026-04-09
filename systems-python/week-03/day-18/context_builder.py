import contextlib

@contextlib.contextmanager
def timer_context(operation_name):
    import time
    print(f"Starting: {operation_name}")
    start = time.time()
    
    try:
        yield
    finally:
        end = time.time()
        print(f"Finished: {operation_name} in {end - start:.4f} seconds")


print("\n--- Timer context manager ---")
with timer_context("fetch barber earnings"):
    import time
    time.sleep(1)
    print("Fetching earnings...")



import threading

class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.active_connections = 0
        self.lock = threading.Lock()

    def get_connection(self):
        with self.lock:
            if self.active_connections >= self.max_connections:
                raise Exception(f"Pool exhausted. All {self.max_connections} connections in use.")
            self.active_connections += 1
            print(f"Connection opened. Active: {self.active_connections}/{self.max_connections}")
            return self.active_connections

    def release_connection(self):
        with self.lock:
            self.active_connections -= 1
            print(f"Connection released. Active: {self.active_connections}/{self.max_connections}")


pool = ConnectionPool(3)


print("\n--- Leaking connections (no context manager) ---")
try:
    conn1 = pool.get_connection()
    conn2 = pool.get_connection()
    conn3 = pool.get_connection()
    conn4 = pool.get_connection()  # This should fail
except Exception as e:
    print(f"ERROR: {e}")

print(f"\nConnections still open after crash: {pool.active_connections}")


@contextlib.contextmanager
def managed_connection(pool):
    connection = pool.get_connection()
    try:
        yield connection
    finally:
        pool.release_connection()


# Reset the pool first
pool.active_connections = 0

print("\n--- Managed connections (with context manager) ---")
try:
    with managed_connection(pool) as conn1:
        with managed_connection(pool) as conn2:
            with managed_connection(pool) as conn3:
                print("All 3 connections in use")
                with managed_connection(pool) as conn4:
                    print("This won't run")
except Exception as e:
    print(f"ERROR: {e}")

print(f"Connections still open after crash: {pool.active_connections}")