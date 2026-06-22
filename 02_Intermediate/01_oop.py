# 01_oop.py
# This script covers Object-Oriented Programming (OOP) concepts.

class Animal:
    """A base class for all animals."""

    # Class attribute
    planet = "Earth"

    def __init__(self, name, species):
        # Instance attributes
        self.name = name
        self.species = species

    def make_sound(self):
        """Method to be overridden by subclasses."""
        return "Generic animal sound"

    def describe(self):
        return f"{self.name} is a {self.species}."

# Inheritance: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ method
        super().__init__(name, species="Dog")
        self.breed = breed

    # Method overriding
    def make_sound(self):
        return "Woof!"

    def describe(self):
        # Extending the parent's describe method
        base_desc = super().describe()
        return f"{base_desc} It is a {self.breed}."

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")

    def make_sound(self):
        return "Meow!"

def main():
    print("--- Basic Class and Objects ---")
    generic_animal = Animal("Creature", "Unknown")
    print(generic_animal.describe())
    print(generic_animal.make_sound())

    print("\n--- Inheritance and Method Overriding ---")
    buddy = Dog("Buddy", "Golden Retriever")
    whiskers = Cat("Whiskers")

    print(buddy.describe())
    print(f"Buddy says: {buddy.make_sound()}")

    print(whiskers.describe())
    print(f"Whiskers says: {whiskers.make_sound()}")

    print("\n--- Class Attributes vs Instance Attributes ---")
    print(f"Buddy is from planet: {buddy.planet}")
    print(f"Whiskers is from planet: {whiskers.planet}")

    # Changing class attribute affects all instances
    Animal.planet = "Mars"
    print(f"After changing Animal.planet...")
    print(f"Buddy is from planet: {buddy.planet}")

if __name__ == "__main__":
    main()
