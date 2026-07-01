
# select user preferences
# - length
# - should contain uppercase letters
# should contain special characters
# - should contain numbers

# get all available characters
# randomly select characters up to the length specified by the user
# ensure that the password contains at least one character from each selected category
# ensure length is valid

import random
import string

def generate_password():
    # Get user preferences
    length = int(input("Enter the desired password length (minimum 8): ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_numbers = input("Include numbers? (yes/no): ").strip().lower()
    
    if length < 8:
        print("Password length must be at least 8 characters.")
        return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
    special_characters = string.punctuation if include_special == 'yes' else ''
    numbers = string.digits if include_numbers == 'yes' else ''
    all_characters = lowercase + uppercase + special_characters + numbers

# Randomly select characters from the combined character set
    required_characters = []
    if include_uppercase == 'yes':
        required_characters.append(random.choice(uppercase))
    if include_special == 'yes':
        required_characters.append(random.choice(special_characters))
    if include_numbers == 'yes':
        required_characters.append(random.choice(numbers))

    # Generate the password
    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
   
    str_password = ''.join(password)
    return str_password


password = generate_password()
print(f"Generated password: {password}")


