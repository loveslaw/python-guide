# test_basic.py
# This script demonstrates testing using pytest.

import pytest

# --- Functions to Test ---

def add(x, y):
    """Adds two numbers."""
    return x + y

def divide(x, y):
    """Divides x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

class StringManipulator:
    def reverse(self, s):
        return s[::-1]

    def capitalize_all(self, words):
        return [w.upper() for w in words]

# --- Tests ---

def test_add_positive_numbers():
    # Arrange & Act
    result = add(3, 4)
    # Assert
    assert result == 7

def test_add_negative_numbers():
    assert add(-2, -5) == -7

def test_add_mixed_numbers():
    assert add(10, -3) == 7

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    # Use pytest.raises to check if an exception is raised
    with pytest.raises(ValueError) as exc_info:
        divide(5, 0)

    # Optional: Check the exception message
    assert "Cannot divide by zero!" in str(exc_info.value)

# --- Using Fixtures ---

# A fixture is a function that runs before tests to provide setup
@pytest.fixture
def string_manip():
    """Returns an instance of StringManipulator."""
    return StringManipulator()

def test_reverse_string(string_manip):
    # string_manip is automatically passed in by pytest
    assert string_manip.reverse("hello") == "olleh"
    assert string_manip.reverse("racecar") == "racecar"

def test_capitalize_all(string_manip):
    input_list = ["apple", "banana"]
    expected = ["APPLE", "BANANA"]
    assert string_manip.capitalize_all(input_list) == expected

# --- Parameterized Tests ---

# Run the same test with different inputs
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (2.5, 2.5, 5.0)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
