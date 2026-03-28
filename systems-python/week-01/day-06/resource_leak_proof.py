import os

# Open 1000 files without closing them
files = []
for i in range(1000):
    f = open("large_test_file.txt", "r")
    files.append(f)

print(f"Opened 1000 file handles")
print(f"Are they closed? {all(f.closed for f in files)}")

# Now try to open even more
try:
    for i in range(10000):
        f = open("large_test_file.txt", "r")
except OSError as e:
    print(f"Error after opening too many files: {e}")

# The right way - context manager guarantees cleanup
print("\nNow doing it the right way:")
with open("large_test_file.txt", "r") as f:
    first_line = f.readline()
    print(f"Read: {first_line.strip()}")
    print(f"Is file closed inside with block? {f.closed}")

print(f"Is file closed outside with block? {f.closed}")