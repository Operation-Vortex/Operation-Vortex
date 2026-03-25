import time

score = 95

# Test 1: 5 separate ifs
start = time.time()
for i in range(10_000_000):
    if score >= 90:
        result = "A"
    if score >= 80:
        result = "B"
    if score >= 70:
        result = "C"
    if score >= 60:
        result = "D"
    if score < 60:
        result = "F"
end = time.time()
print(f"5 separate ifs: {end - start:.4f} seconds")

# Test 2: if/elif/else
start = time.time()
for i in range(10_000_000):
    if score >= 90:
        result = "A"
    elif score >= 80:
        result = "B"
    elif score >= 70:
        result = "C"
    elif score >= 60:
        result = "D"
    else:
        result = "F"
end = time.time()
print(f"if/elif/else: {end - start:.4f} seconds")