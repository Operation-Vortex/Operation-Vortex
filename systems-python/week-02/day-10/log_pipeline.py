import sys
import tracemalloc

tracemalloc.start()

# EAGER: Load everything into memory
with open("systems-python/week-02/day-10/server.log", "r") as f:
    all_lines = f.readlines()

# Filter only ERROR lines
errors = [line for line in all_lines if "[ERROR]" in line]

# Transform — extract just the time and message
cleaned = [line.split("] ")[1].strip() for line in errors]

print(f"Total errors: {len(cleaned)}")
print(f"First 3: {cleaned[:3]}")
print(f"Memory used: {tracemalloc.get_traced_memory()[1] / 1_000_000:.2f} MB")

tracemalloc.stop()


print("\n--- Generator approach ---")

tracemalloc.start()

def read_lines(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line

def filter_errors(lines):
    for line in lines:
        if "[ERROR]" in line:
            yield line

def extract_message(lines):
    for line in lines:
        yield line.split("] ")[1].strip()

# Build the pipeline — nothing runs yet
lines = read_lines("systems-python/week-02/day-10/server.log")
errors = filter_errors(lines)
messages = extract_message(errors)

# NOW it runs — one line at a time through the whole chain
count = 0
first_three = []

for message in messages:
    count += 1
    if count <= 3:
        first_three.append(message)

print(f"Total errors: {count}")
print(f"First 3: {first_three}")
print(f"Memory used: {tracemalloc.get_traced_memory()[1] / 1_000_000:.2f} MB")

tracemalloc.stop()