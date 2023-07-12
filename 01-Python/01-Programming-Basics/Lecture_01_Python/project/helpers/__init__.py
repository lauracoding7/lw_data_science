import random
import string

# Define function
def generate_password(size):
    """Generate a random lowercase ASCII password of given size"""
    letters = string.ascii_lowercase
    # breakpoint()
    return ''.join(random.choice(letters) for i in range(size))
