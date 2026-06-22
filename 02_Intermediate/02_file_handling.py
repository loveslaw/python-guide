# 02_file_handling.py
# This script covers reading and writing files.
import os

def main():
    filename = "sample_file.txt"

    print("--- Writing to a File ---")
    # Using 'w' mode (write): overwrites file if it exists, creates if it doesn't
    with open(filename, 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line.\n")
    print(f"Successfully wrote to {filename}")

    print("\n--- Reading from a File ---")
    # Using 'r' mode (read): default mode
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents using read():")
        print(content)

    print("--- Appending to a File ---")
    # Using 'a' mode (append): adds to the end of the file
    with open(filename, 'a') as file:
        file.write("This line was appended.\n")
    print(f"Successfully appended to {filename}")

    print("\n--- Reading Line by Line ---")
    with open(filename, 'r') as file:
        print("File contents line by line:")
        for line in file:
            # end='' prevents printing an extra newline since the line already has one
            print(f"- {line}", end='')

    print("\n\n--- Cleaning Up ---")
    # Delete the file we created
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")

if __name__ == "__main__":
    main()
