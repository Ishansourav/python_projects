import random
import string

def generate_random_password(length=16, use_lowercase=True, use_uppercase=True,
                             use_digits=True, use_special_chars=True):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set (lowercase, uppercase, digits, or special characters) must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a random password with 20 characters, using lowercase, uppercase, digits, and special characters
random_password = generate_random_password(20)
print("Random Password:", random_password)

