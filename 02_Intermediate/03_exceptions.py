# 03_exceptions.py
# This script covers error handling using try/except blocks.

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero!")
        return None
    except TypeError:
        print(f"Error: Both arguments must be numbers. Got '{a}' and '{b}'")
        return None
    else:
        # The else block executes ONLY if no exception occurred
        print("Division successful.")
        return result
    finally:
        # The finally block ALWAYS executes, regardless of whether an exception occurred
        print("Execution of divide_numbers completed.")

# Custom Exception
class NegativeNumberError(Exception):
    """Raised when a negative number is provided but not allowed."""
    pass

def process_positive_number(num):
    if num < 0:
        # Raise our custom exception
        raise NegativeNumberError(f"Number cannot be negative, got: {num}")
    return num * 2

def main():
    print("--- Handling Specific Exceptions ---")
    print("\nScenario 1: Valid division")
    res1 = divide_numbers(10, 2)
    print(f"Result: {res1}")

    print("\nScenario 2: Division by zero")
    res2 = divide_numbers(10, 0)
    print(f"Result: {res2}")

    print("\nScenario 3: Type error")
    res3 = divide_numbers(10, "two")
    print(f"Result: {res3}")

    print("\n--- Raising Exceptions ---")
    try:
        print(f"Processing 5: {process_positive_number(5)}")
        print(f"Processing -3: {process_positive_number(-3)}")
    except NegativeNumberError as e:
        print(f"Caught custom exception: {e}")
    except Exception as e:
        # Catch-all for any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
