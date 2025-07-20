def password_strength(password):
    point = 0

    special_characters = "!@#$%^&*()_{}|?~[]/.,';\""

    if len(password) >= 8:
        point += 1

    if any(char.isupper() for char in password):
        point += 1

    if any(char.islower() for char in password):
        point += 1

    if any(char.isdigit() for char in password):
        point += 1

    if any(char in special_characters for char in password):
        point += 1

    if point <= 2:
        return "Weak password"
    elif point == 3 or point == 4:
        return "Medium password"
    else:
        return "Strong password"

def main():
    password = input("Enter a password: ")
    strength = password_strength(password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
