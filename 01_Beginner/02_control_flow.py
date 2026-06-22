# 02_control_flow.py
# This script covers if/else statements and loops.

def main():
    print("--- If/Elif/Else Statements ---")

    age = 20
    print(f"Age is {age}")

    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")

    print("\n--- For Loops ---")

    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    print("Iterating over a list:")
    for fruit in fruits:
        print(f"- {fruit}")

    # Iterating over a range of numbers
    print("\nIterating over a range(5):")
    for i in range(5): # Generates numbers from 0 to 4
        print(i)

    # Iterating over a dictionary
    person = {"name": "Bob", "age": 25, "job": "Developer"}
    print("\nIterating over dictionary key-value pairs:")
    for key, value in person.items():
        print(f"{key}: {value}")

    print("\n--- While Loops ---")

    counter = 0
    while counter < 3:
        print(f"Counter is {counter}")
        counter += 1 # Important to increment to avoid infinite loops

    print("\n--- Break and Continue ---")

    print("Using break (stops at 3):")
    for i in range(5):
        if i == 3:
            break
        print(i)

    print("\nUsing continue (skips 2):")
    for i in range(5):
        if i == 2:
            continue
        print(i)

if __name__ == "__main__":
    main()
