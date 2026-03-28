import time

file_path = "/Users/mackook/Development/Operation-Vortex/systems-python/week-01/day-06/large_test_file.txt"

# Method 1: read() - entire file at once
start = time.time()
with open(file_path, 'r') as file:
    content = file.read()
end = time.time()
print(f"read() - entire file: {end - start:.4f} seconds")

# Method 2: readlines() - entire file as list
start = time.time()
with open(file_path, 'r') as file:
    lines = file.readlines()
end = time.time()
print(f"readlines() - as list: {end - start:.4f} seconds")

# Method 3: readline() - line by line
start = time.time()
with open(file_path, 'r') as file:
    line = file.readline()
    while line:
        line = file.readline()
end = time.time()
print(f"readline() - line by line: {end - start:.4f} seconds")