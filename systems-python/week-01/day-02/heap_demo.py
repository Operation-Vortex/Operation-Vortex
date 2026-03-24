import sys
import os

numbers = list(range(1_000_000))
print(f"List created: {len(numbers)} numbers")
print(f"List size in memory: {sys.getsizeof(numbers)} bytes")
print(f"Process memory usage: check Activity Monitor")

input("Press Enter to delete the list...")

del numbers
import gc
gc.collect()

print("List deleted")
input("Press Enter to exit...")

