
import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a random password with the default length of 12 characters
random_password = generate_random_password()
print("Random Password:", random_password)

