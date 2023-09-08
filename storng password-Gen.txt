import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters to choose from
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure each character set is included in the password
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(digits),
                random.choice(special_characters)]

    # Fill the remaining characters randomly
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    # Shuffle the characters to make the password more random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

# Usage:
strong_password = generate_password()
print("Strong Password:", strong_password)

