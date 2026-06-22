# 02_generators.py
# This script covers generators and the yield keyword.

import sys

def count_up_to(max_value):
    """A simple generator function."""
    count = 1
    while count <= max_value:
        # yield pauses execution and returns the value
        # execution resumes here on the next next() call
        yield count
        count += 1

def fibonacci_generator():
    """An infinite generator for the Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    print("--- Basic Generator ---")
    # Calling a generator function returns a generator object
    counter = count_up_to(3)
    print(f"Type of counter: {type(counter)}")

    # Extracting values using next()
    print(next(counter)) # 1
    print(next(counter)) # 2
    print(next(counter)) # 3

    # Uncommenting the next line would raise StopIteration
    # print(next(counter))

    print("\n--- Iterating over a Generator ---")
    # A cleaner way to consume a generator is with a for loop
    for num in count_up_to(5):
        print(num, end=" ")
    print() # newline

    print("\n--- Infinite Generator ---")
    fib = fibonacci_generator()
    print("First 10 Fibonacci numbers:")
    for _ in range(10):
        print(next(fib), end=" ")
    print()

    print("\n--- Generators vs Lists (Memory Efficiency) ---")
    # Generators are lazy-evaluated, making them highly memory efficient for large sequences
    n = 1_000_000

    # List comprehension creates the entire list in memory
    list_comp = [i * 2 for i in range(n)]

    # Generator expression creates an iterator
    gen_expr = (i * 2 for i in range(n))

    print(f"Size of list comprehension in memory: {sys.getsizeof(list_comp)} bytes")
    print(f"Size of generator expression in memory: {sys.getsizeof(gen_expr)} bytes")

if __name__ == "__main__":
    main()
