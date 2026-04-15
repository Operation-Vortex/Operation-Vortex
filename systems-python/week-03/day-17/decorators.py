import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@logger
def get_earnings():
    print("Calculating earnings...")


get_earnings()  


@logger
def get_barber_earnings(barber_id, month):
    print(f"Calculating earnings for barber {barber_id} in month {month}")

get_barber_earnings("B001", "April")
print(get_barber_earnings.__name__)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timer
def slowCalculation(n):
    total = 0
    for i in range(n):
        total += i 
    return total

result = slowCalculation(1000000)
print(f"Result: {result}")


def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token", None)
        if token != "valid_token_123":
            print("Access denied. Invalid or missing token.")
            return None
        return func(*args, **kwargs)
    return wrapper



@require_auth
def get_earnings(barber_id, token=None):
    print(f"Earnings for barber {barber_id}: GHS 450")

get_earnings("B001", token="wrong_token")
get_earnings("B001", token="valid_token_123")


import functools
import time

def slow_fibonacci(n):
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

start = time.time()
print(slow_fibonacci(35))
print(f"Without cache: {time.time() - start:.4f} seconds")

@functools.lru_cache(maxsize=None)
def fast_fibonacci(n):
    if n < 2:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)

start = time.time()
print(fast_fibonacci(35))
print(f"With cache: {time.time() - start:.4f} seconds")