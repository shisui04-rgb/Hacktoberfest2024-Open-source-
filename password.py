import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """Generate a random password."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
length = 16
use_uppercase = True
use_numbers = True
use_special_chars = True

password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
print(f"Generated password: {password}")
