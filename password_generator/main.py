import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += numbers
    if special:
        characters += special

    pwd = ""

    meets_criteria = False

    has_number = False

    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in numbers:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = (
                meets_criteria and has_special
            )  # true if both meets_criteria and has_special are both true

    return pwd


min_length = int(input("Enter the minimum length:  "))
has_number = input("Do you want any numbers (y/n)? ").lower() == "y"
has_special = input("Do you want any special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is: ", pwd)
