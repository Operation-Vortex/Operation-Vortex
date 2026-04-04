# Open the file and read all lines
with open("/Users/mackook/Development/Operation-Vortex/systems-python/week-02/day-09/sample_text.txt", "r") as file:
    full_text = file.read()

# Split the long string into words
words = full_text.split()

# Create an empty dictionary
word_bank_and_count_map = {}

# Loop through the words and count them
for individual_word in words:
    word = individual_word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_bank_and_count_map:
        word_bank_and_count_map[word] = word_bank_and_count_map[word] + 1
    else:
        word_bank_and_count_map[word] = 1

# Print the results
for word in word_bank_and_count_map:
    print(word, ":", word_bank_and_count_map[word])