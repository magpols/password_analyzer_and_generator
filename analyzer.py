# Check the length of the password
def check_length(password):
    length = len(password)

    if length >= 12:
        return True
    else:
        return False


# Check if the password has any uppercase character
def check_uppercase(password):
    for character in password:
        if character.isupper():
            return True

    return False


# Check if the password has any lowercase character
def check_lowercase(password):
    for character in password:
        if character.islower():
            return True

    return False


# Check if the password has any special symbol
def check_symbol(password):
    for character in password:
        if not character.isalnum():
            return True

    return False


# Check if the password has any number
def check_number(password):
    for character in password:
        if character.isdigit():
            return True

    return False


# A small sample list of common passwords
common_passwords = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "letmein"
}


# Check if the password is a common password
def check_common_password(password):
    return password.lower() in common_passwords


# Check if the password has repeated characters
def has_repeated_characters(password, repeat_limit=3):

    count = 1

    for i in range(1, len(password)):

        if password[i] == password[i - 1]:
            count += 1

            if count >= repeat_limit:
                return True

        else:
            count = 1

    return False


# Calculate the score of the password
def calculate_score(password):
    score = 0

    if check_length(password):
        score += 25

    if check_uppercase(password):
        score += 15

    if check_lowercase(password):
        score += 15

    if check_number(password):
        score += 15

    if check_symbol(password):
        score += 20

    if len(password) >= 16:
        score += 10

    return score


# Convert the score into a rating
def get_rating(score):

    if score < 40:
        return "Weak"

    if score < 60:
        return "Fair"

    if score < 80:
        return "Good"

    if score < 100:
        return "Strong"

    return "Very Strong"


# Create one master function
def analyze_password(password):

    score = calculate_score(password)

    result = {
        "length": len(password),
        "has_uppercase": check_uppercase(password),
        "has_lowercase": check_lowercase(password),
        "has_number": check_number(password),
        "has_symbol": check_symbol(password),
        "is_common_password": check_common_password(password),
        "has_repeated_characters": has_repeated_characters(password),
        "score": score,
        "rating": get_rating(score)
    }

    return result