# 03_context_managers.py
# This script covers context managers (the 'with' statement).

import os
from contextlib import contextmanager

# 1. Context Manager using a Class
class ManagedFile:
    """A custom context manager for file handling, mimicking built-in 'open'."""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Executed when entering the 'with' block."""
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file # This is bound to the variable after 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Executed when exiting the 'with' block, even if an exception occurred."""
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()

        # If an exception occurred, exc_type, exc_val, and exc_tb will contain info
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred: {exc_val}")
            # Return True to suppress the exception, False (or None) to propagate it
            # We'll return False so the caller still sees the error
            return False

# 2. Context Manager using a Generator (contextlib)
@contextmanager
def temporary_file(filename):
    """A context manager that creates a file and deletes it after use."""
    print(f"Creating temp file: {filename}")
    f = open(filename, 'w')
    try:
        # The value yielded is bound to the variable after 'as'
        yield f
    finally:
        # This block corresponds to __exit__
        print(f"Cleaning up temp file: {filename}")
        f.close()
        if os.path.exists(filename):
            os.remove(filename)

def main():
    print("--- Class-based Context Manager ---")
    test_file = "test.txt"

    # Write using our custom manager
    with ManagedFile(test_file, 'w') as f:
        f.write("Testing custom context manager.")
        # f is automatically closed at the end of this block

    # Read and clean up
    with ManagedFile(test_file, 'r') as f:
        print(f"File contents: {f.read()}")
    os.remove(test_file)

    print("\n--- Generator-based Context Manager ---")
    with temporary_file("temp.txt") as temp:
        temp.write("Some temporary data.")
        print("Wrote to temp file.")
        # Notice we don't need to manually delete it; the context manager handles it

    print("\n--- Exception Handling in Context Managers ---")
    try:
        with ManagedFile("another_test.txt", 'w') as f:
            f.write("Starting to write...")
            raise ValueError("Something went wrong during write!")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    finally:
         if os.path.exists("another_test.txt"):
             os.remove("another_test.txt")

if __name__ == "__main__":
    main()
