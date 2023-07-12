# CRUD OPERARIONS FOR LISTS AND DICTIONARIES

### LISTS ###
# Lists are the most basic and commonly used sequence type in Python.
# Lists are sometimes referred to as "arrays" in other programming languages.
# You define a list with square brackets [] or the list() function.

# CREATE
fruits = []
fruits.append("strawberry")

# READ
fruits[0]

# UPDATE
fruits[0] = "mango"

# DELETE
del fruits[0]

### DICTIONARIES ###
# Dictionaries (dict) are Python's mapping type
# You define a dict with curly braces {} or the dict() function
# They are composed of {Key: Value} pairs

# CREATE
animals = {}
animals["dog"] = "woof"

# READ
animals["dog"]

# UPDATE
animals["dog"] = "woof woof"

# DELETE
del animals["dog"]
