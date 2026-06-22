# 03_functions.py
# This script covers defining and using functions.

# Basic function
def greet():
    """This function just prints a greeting."""
    print("Hello there!")

# Function with arguments
def greet_person(name):
    """Greets a specific person."""
    print(f"Hello, {name}!")

# Function with default arguments
def greet_with_default(name="Guest"):
    """Greets a person, defaults to Guest if no name provided."""
    print(f"Welcome, {name}!")

# Function returning a value
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Function with multiple return values (returns a tuple)
def get_user_info():
    """Returns name and age."""
    return "Alice", 30

# Function with arbitrary positional arguments (*args)
def sum_all(*args):
    """Sums any number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

# Function with arbitrary keyword arguments (**kwargs)
def print_info(**kwargs):
    """Prints key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    print("--- Functions ---")
    greet()
    greet_person("Bob")
    greet_with_default()
    greet_with_default("Charlie")

    print("\n--- Return Values ---")
    result = add_numbers(5, 7)
    print(f"5 + 7 = {result}")

    name, age = get_user_info()
    print(f"Got info: Name={name}, Age={age}")

    print("\n--- *args and **kwargs ---")
    print(f"Sum of 1, 2, 3, 4: {sum_all(1, 2, 3, 4)}")

    print("Printing info:")
    print_info(first_name="John", last_name="Doe", occupation="Engineer")

if __name__ == "__main__":
    main()
