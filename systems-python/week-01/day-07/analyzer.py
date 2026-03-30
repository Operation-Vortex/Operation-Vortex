import sys
from pathlib import Path

def format_size(size_in_bytes):
    if size_in_bytes < 1024:
        return str(size_in_bytes) + " B"
    elif size_in_bytes < 1024 * 1024:
        size_in_kb = size_in_bytes / 1024
        return str(round(size_in_kb, 2)) + " KB"
    else:
        size_in_mb = size_in_bytes / (1024 * 1024)
        return str(round(size_in_mb, 2)) + " MB"
    
def validate_path(directory_path):
    if not directory_path.exists():
        print("Error: Path does not exist")
        return False
    if not directory_path.is_dir():
        print("Error: Path is not a directory")
        return False
    return True


def analyze_directory(directory_path):
    total_files = 0
    total_size = 0
    largest_file = None
    largest_file_size = 0
    extension_type_dictionary = {}
    try:
        for current_item_under_iteration in directory_path.iterdir():
            if current_item_under_iteration.is_file():
                total_files = total_files + 1
                current_item_size = current_item_under_iteration.stat().st_size
                total_size = total_size + current_item_size
                if current_item_size > largest_file_size:
                    largest_file_size = current_item_size
                    largest_file = current_item_under_iteration
                file_extension = current_item_under_iteration.suffix
                if file_extension == "":
                    file_extension = "[no extension]"
                if file_extension in extension_type_dictionary:
                    extension_type_dictionary[file_extension] = (
                        extension_type_dictionary[file_extension] + 1
                    )
                else:
                    extension_type_dictionary[file_extension] = 1
    except Exception:
        print("Error: Unable to access directory contents (permission issue).")
        return None
    return total_files, total_size, largest_file, largest_file_size, extension_type_dictionary


def print_report(directory_path, total_files, total_size, largest_file, largest_file_size, extension_type_dictionary, summary_mode):
    if summary_mode:
        print(
            "Directory:",
            directory_path.resolve(),
            "| Files:",
            total_files,
            "| Size:",
            format_size(total_size)
        )
        return
    print("\nFILE SYSTEM ANALYSIS")
    print("--------------------")
    print("Directory:", directory_path.resolve())
    print("Total files:", total_files)
    print("Total size:", format_size(total_size))
    if largest_file is not None:
        print("Largest file:", largest_file.name)
        print("Largest size:", format_size(largest_file_size))
    else:
        print("Largest file: None")
        print("Largest size: 0 B")
    print("\nFile type breakdown:")
    for file_extension in extension_type_dictionary:
        print(file_extension, ":", extension_type_dictionary[file_extension])

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <path> [--summary]")
        return
    user_input_path = sys.argv[1]
    directory_path = Path(user_input_path)
    summary_mode = "--summary" in sys.argv
    if not validate_path(directory_path):
        return
    analysis_result = analyze_directory(directory_path)
    if analysis_result is None:
        return
    total_files, total_size, largest_file, largest_file_size, extension_type_dictionary = analysis_result
    print_report(
        directory_path,
        total_files,
        total_size,
        largest_file,
        largest_file_size,
        extension_type_dictionary,
        summary_mode
    )

main()