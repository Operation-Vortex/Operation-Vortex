import sys

d = {}
prev_size = sys.getsizeof(d)

for i in range(20):
    d[f"key_{i}"] = i
    current_size = sys.getsizeof(d)
    if current_size != prev_size:
        print(f"Added key_{i} → size jumped from {prev_size} to {current_size} bytes ({len(d)} items)")
        prev_size = current_size