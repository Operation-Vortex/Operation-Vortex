from time import perf_counter


sizes = [1_000, 10_000, 100_000]

for size in sizes:
    # Create list and set with numbers 0 to 99,999
    numbers_list = list(range(size))
    numbers_set = set(range(size))

    target_number = size - 1

# Time list lookup
    list_start_time = perf_counter()
    target_number in numbers_list
    list_end_time = perf_counter()

    ist_lookup_time = list_end_time - list_start_time

# Time set lookup
    set_start_time = perf_counter()
    target_number in numbers_set
    set_end_time = perf_counter()

    set_lookup_time = set_end_time - set_start_time


    print(f'List lookup time for size {size}: {ist_lookup_time:.10f} seconds')
    print(f'Set lookup time for size {size}:  {set_lookup_time:.10f} seconds')