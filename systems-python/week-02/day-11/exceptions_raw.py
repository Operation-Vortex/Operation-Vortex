

def file_reader(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except PermissionError :
        print(f"You are not permitted to view the file '{file_name}'.")
    except UnicodeDecodeError:
        print(f"The file '{file_name}' is not a text file.");



print("Reading existing file:")
file_reader("systems-python/week-02/day-11/exceptions_raw.py")


print("\nReading non-existent file:")
file_reader("systems-python/week-02/day-11/non_existent_file.txt")
#file_reader("systems-python/week-02/day-11/non_existent_file.txt")ß