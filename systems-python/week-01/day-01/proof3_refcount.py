# PROOF 3: Reference counting in action
import sys

x = 10000
print("=== Reference Counting ===")
print(f"One label pointing at 10000")
print(f"Refcount: {sys.getrefcount(x) - 1}")

y = x
print(f"\nTwo labels now pointing at same object")
print(f"Refcount: {sys.getrefcount(x) - 1}")

y = None
print(f"\nOne label removed")
print(f"Refcount: {sys.getrefcount(x) - 1}")

print("\nWhen refcount hits 0, object is destroyed.")
print("That is how Python manages memory.")