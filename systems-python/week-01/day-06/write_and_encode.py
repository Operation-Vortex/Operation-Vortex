# Writing to a file

file_path_1 = '/Users/mackook/Development/Operation-Vortex/systems-python/week-01/day-06/write_and_encode.txt'
file_path_2 = '/Users/mackook/Development/Operation-Vortex/systems-python/week-01/day-06/unicode_test.txt'

with open(file_path_1, "w") as f:
    f.write("Hello World\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print("File written successfully")

# Reading it back
with open(file_path_1, "r") as f:
    content = f.read()
    print(content)

# Now encoding - write some special characters
with open(file_path_2, "w", encoding="utf-8") as f:
    f.write("English: Hello\n")
    f.write("Arabic: مرحبا\n")
    f.write("Chinese: 你好\n")
    f.write("Emoji: 🔥\n")

print("Unicode file written")

# Read it back
with open(file_path_2, "r", encoding="utf-8") as f:
    print(f.read())