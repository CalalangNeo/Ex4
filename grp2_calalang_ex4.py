# Task 1: If statement: true or false

def check_number(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Test the function
result = check_number(4)  # True because 4 is even
print(result)

# Task 2: List, tuples, sets and dictionaries

# List: Ordered, changeable, allows duplicates.
my_list = ["red", 99, False, "circle"]  
print("List:", my_list)

# Tuple: Ordered, unchangeable (immutable), allows duplicates.

my_tuple = ("blue", 25, True, "square") 
print("Tuple:", my_tuple)

# Set: Unordered, unindexed, no duplicates allowed.
my_set = {"triangle", 55, True, "green"}  
print("Set:", my_set)

# Dictionary: A collection of key-value pairs. It is ordered (as of Python 3.7+), changeable, and doesn't allow duplicate keys.
my_dict = {
    "name": "Neo",   # String
    "age": 21,         # Integer
    "is_a_student": True,  # Boolean
    "city": "Muntinlupa",  # String
    "years_level": 3  # Integer
    
}
print("Dictionary:", my_dict)
