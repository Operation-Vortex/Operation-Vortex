# PROOF 1: Variables are labels, not boxes
x = 10000
y = 10000

print("=== Variables are Labels, Not Boxes ===")
print(f"x = {x}, memory address: {id(x)}")
print(f"y = {y}, memory address: {id(y)}")
print(f"Same address? {id(x) == id(y)}")
print("Two names. One object in memory.")