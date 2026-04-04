import random
import string

with open("big_text.txt", "w") as f:
    for i in range(1_000_000):
        word = ''.join(random.choices(string.ascii_lowercase, k=5))
        f.write(word + " ")

print("Done. 1 million random words written.")