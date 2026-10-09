import random
import string

# Need to ask how many characters needed for the password
def get_password_length():

    while True:
        try:
            length = int(input("How many characters: "))

            if length < 12:
                print("Password should have at leat 12 characters. Please try again.")
                continue

            return length

        except ValueError:
            print("Please enter a valid while number.")

def generate_password(length):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    letters = uppercase + lowercase
    all_characters = uppercase + lowercase + numbers + symbols

    # First character must be a letter
    password = random.choice(letters)

    while len(password) < length:

        character = random.choice(all_characters)

        # Same character cannot appear next
        if character == password[-1]:
            continue

        # Same character cannot appear more than twice
        if password.count(character) >= 2:
            continue

        password += character

    # Check required character types:
    has_uppercase = any(character.isupper() for character in password)
    has_lowercase = any(character.islower() for character in password)
    has_number = any(character.isdigit() for character in password)
    has_symbol = any(not character.isalnum() for character in password)

    if (
        has_uppercase
        and has_lowercase
        and has_number
        and has_symbol
    ):
        return password

    # Generate again if any requirement is missing
    return generate_password(length)

password_length = get_password_length()

password = generate_password(password_length)

print("Generated password: ", password)
