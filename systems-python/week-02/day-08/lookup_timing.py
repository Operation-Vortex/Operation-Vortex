import time

# Create list and set with numbers 0 to 99,999
numbers_list = list(range(100_000))
numbers_set = set(range(100_000))

target_number = 99_999

# Time list lookup
list_start_time = time.perf_counter()
target_number in numbers_list
list_end_time = time.perf_counter()

list_lookup_time = list_end_time - list_start_time

# Time set lookup
set_start_time = time.perf_counter()
target_number in numbers_set
set_end_time = time.perf_counter()

set_lookup_time = set_end_time - set_start_time

print(f'List lookup time: {list_lookup_time:.10f} seconds')
print(f'Set lookup time:  {set_lookup_time:.10f} seconds')