# Function are pieces of reuseable python code
# If you find yourself doing the same thing multiple times,
# chances are you could turn this process into a function

# Function definition
def is_even(number): # one positional parameter
    # RETURN otherwise the function doesn't "give" you anything
    # (it only prints out stuff to the terminal)
    return number % 2 == 0

# Function call and store the output in a variable called result
result = is_even(42) # need to pass one positional argument
print(result)


def is_odd(number=0): # one keyword parameter (with default value)
    return number % 2 == 1

# Function call and store the output in a variable called result
result = is_odd(number=1) # optional keyword argument
print(result)

# First define positional parameters, and then all the optional keyword parameters
def full_name(first_name, last_name, capitalize=False):
    if capitalize:
        return f"{first_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name} {last_name}"

# both work
print(full_name("john", "lennon"))
print(full_name("ringo", "starr", capitalize=True))
