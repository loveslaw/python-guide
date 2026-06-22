# 01_decorators.py
# This script covers function decorators.

import time
from functools import wraps

# A simple decorator
def my_simple_decorator(func):
    """A basic decorator that prints before and after calling the function."""
    @wraps(func) # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        print(f"Something is happening before the function '{func.__name__}' is called.")
        result = func(*args, **kwargs)
        print(f"Something is happening after the function '{func.__name__}' is called.")
        return result
    return wrapper

# A more practical decorator: execution timer
def timer_decorator(func):
    """Measures the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Using decorators
@my_simple_decorator
def say_hello(name):
    """Prints a simple greeting."""
    print(f"Hello, {name}!")

@timer_decorator
def slow_function(delay):
    """Simulates a time-consuming task."""
    print(f"Sleeping for {delay} seconds...")
    time.sleep(delay)
    return "Done sleeping"

# Applying multiple decorators (applied from bottom to top)
@my_simple_decorator
@timer_decorator
def complex_operation():
    time.sleep(0.5)
    print("Operation complete.")

def main():
    print("--- Simple Decorator ---")
    say_hello("Alice")

    # Notice that __name__ and __doc__ are preserved due to @wraps
    print(f"Function name: {say_hello.__name__}")
    print(f"Docstring: {say_hello.__doc__}")

    print("\n--- Timer Decorator ---")
    result = slow_function(1)
    print(f"Result: {result}")

    print("\n--- Multiple Decorators ---")
    complex_operation()

if __name__ == "__main__":
    main()
