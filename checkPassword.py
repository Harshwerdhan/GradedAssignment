# Write function to return password is strong or not
def check_password_strength(password : str) -> bool:
    # Check for criteria
    password_length_is_ok = len(password) >= 8
    password_has_upper = any(char.isupper() for char in password)
    password_has_lower = any(char.islower() for char in password)
    password_has_digit = any(char.isdigit() for char in password)
    
    special_char_list = '''!@#$%^&*(),.?":{}|<> '''
    password_has_special_char = any(char in special_char_list for char in password)

    return all([password_length_is_ok,password_has_upper,password_has_lower,password_has_digit,password_has_special_char])


input_password = input("Enter your password: ")

if check_password_strength(input_password):
    print("Password is strong")
else:
    print("Your password is weak")
    print("===== Ensure password should meets these criteria =====")
    print("-- At least 8 characters")
    print("-- Contains both uppercase and lowercase letters")
    print("-- Contails at least one digit (0-9)")
    print("-- Contain at least one special character")