square = []

for x in range(10):
    square.append(x*x)

print(square)



# --- List comprehension ---
squares = [x * x for x in range(10)]
print(squares)


squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)