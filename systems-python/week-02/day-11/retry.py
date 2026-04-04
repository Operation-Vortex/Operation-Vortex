import random
from time import sleep

def call_api():
    if random.random() < 0.7:
        raise ConnectionError("Server not responding")
    return "Success! Data received."

def retry_call(func, max_attempts):
    for attempt in range(1, max_attempts + 1):
        try:
            result = func()
            print(f"Attempt {attempt}: {result}")
            return result
        except ConnectionError as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
               wait_time = 2 * attempt
               print(f"Retrying in {wait_time} seconds...")
               sleep(wait_time)

    print("All attempts failed.")

retry_call(call_api, 3)


