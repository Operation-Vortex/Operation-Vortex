# Python uses the hash to decide the bucket
# Let's simulate buckets with modulo, like yesterday

num_buckets = 4

words = ["hello", "world", "python", "data", "hash", "set", "dict", "list"]

for word in words:
    bucket = hash(word) % num_buckets
    print(f"{word:10} → bucket {bucket}")