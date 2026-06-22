# 01_variables.py
# This script covers basic data types, variables, and operators in Python.

def main():
    print("--- Variables and Data Types ---")

    # Integers (whole numbers)
    my_integer = 10
    print(f"Integer: {my_integer}, Type: {type(my_integer)}")

    # Floats (decimal numbers)
    my_float = 3.14159
    print(f"Float: {my_float}, Type: {type(my_float)}")

    # Strings (text)
    my_string = "Hello, Python!"
    print(f"String: '{my_string}', Type: {type(my_string)}")

    # Booleans (True or False)
    is_python_fun = True
    print(f"Boolean: {is_python_fun}, Type: {type(is_python_fun)}")

    print("\n--- Basic Operators ---")

    # Arithmetic operators
    a = 15
    b = 4

    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b): {a + b}")
    print(f"Subtraction (a - b): {a - b}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"Division (a / b): {a / b}") # Always returns a float
    print(f"Integer Division (a // b): {a // b}") # Floors the result
    print(f"Modulo (a % b): {a % b}") # Remainder
    print(f"Exponentiation (a ** b): {a ** b}")

    print("\n--- Basic Data Structures ---")

    # Lists (ordered, mutable collection)
    my_list = [1, 2, 3, "apple", "banana"]
    print(f"List: {my_list}")
    my_list.append("cherry")
    print(f"List after append: {my_list}")

    # Tuples (ordered, immutable collection)
    my_tuple = (10, 20, 30)
    print(f"Tuple: {my_tuple}")
    # my_tuple[0] = 15  # This would raise a TypeError because tuples are immutable

    # Dictionaries (key-value pairs, unordered)
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Dictionary: {my_dict}")
    print(f"Name from dict: {my_dict['name']}")

    # Sets (unordered collection of unique elements)
    my_set = {1, 2, 2, 3, 4, 4, 5}
    print(f"Set (notice duplicates are removed): {my_set}")

if __name__ == "__main__":
    main()
