from time import sleep, perf_counter

# --- Slow version ---
def get_exchange_rate(currency):
    print(f"Fetching rate for {currency}...")
    sleep(2)
    rates = {"USD": 12.5, "GBP": 15.8, "EUR": 13.2}
    return rates.get(currency, 0)

# --- Cached version ---
cache = {}

def get_exchange_rate_cached(currency):
    if currency in cache:
        print(f"Cache hit for {currency}!")
        return cache[currency]
    print(f"Fetching rate for {currency}...")
    sleep(2)
    rates = {"USD": 12.5, "GBP": 15.8, "EUR": 13.2}
    result = rates.get(currency, 0)
    cache[currency] = result
    return result

# --- Test slow version ---
print("=== Without cache ===")
start = perf_counter()
get_exchange_rate("USD")
get_exchange_rate("USD")
get_exchange_rate("USD")
slow_time = perf_counter() - start
print(f"Total: {slow_time:.2f} seconds\n")

# --- Test cached version ---
print("=== With cache ===")
start = perf_counter()
get_exchange_rate_cached("USD")
get_exchange_rate_cached("USD")
get_exchange_rate_cached("USD")
fast_time = perf_counter() - start
print(f"Total: {fast_time:.2f} seconds")