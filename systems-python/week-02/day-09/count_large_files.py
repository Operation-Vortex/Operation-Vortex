from time import perf_counter

# Read the big file
with open("/Users/mackook/Development/Operation-Vortex/big_text.txt", "r") as f:
    words = f.read().split()

print(f"Total words: {len(words)}")

# ---- APPROACH 1: Dict ----
start = perf_counter()

dict_counter = {}

for word in words:
    word = word.lower()
    if word in dict_counter:
        dict_counter[word] = dict_counter[word] + 1
    else:
        dict_counter[word] = 1

dict_time = perf_counter() - start
print(f"Dict approach: {dict_time:.4f} seconds")

# ---- APPROACH 2: List of tuples ----
start = perf_counter()

list_counter = []
for word in words:
    word = word.lower()
    found = False
    for i in range(len(list_counter)):
        if list_counter[i][0] == word:
            list_counter[i] = (word, list_counter[i][1] + 1)
            found = True
            break
    if not found:
        list_counter.append((word, 1))

list_time = perf_counter() - start
print(f"List approach: {list_time:.4f} seconds")

print(f"Dict was {list_time / dict_time:.1f}x faster")