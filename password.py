import string
import random

def password_gen(length):

    # Possible characters that are allowed in password
    # Includes upper and lower case letters, numbers, and punctuation
    possible_chars = string.ascii_letters + string.digits + string.punctuation

    # Use Python 3.6 random.choices to create password from possible characters
