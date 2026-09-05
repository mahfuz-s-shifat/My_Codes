import re
import secrets
import string
import sys

UPPERCASE_CHARS = string.ascii_uppercase
LOWERCASE_CHARS = string.ascii_lowercase
DIGIT_CHARS = string.digits
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}?"

MIN_PASSWORD_LENGTH = 8

COMMON_WEAK_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123",
    "password123",
    "123456789",
    "iloveyou",
    "monkey",
    "dragon",
}

SEQUENTIAL_NUMBER_PATTERNS = [
    "123", "234", "345", "456", "567", "678", "789", "012", "890"
]

def generate_password(
    length: int = 16,
    uppercase: bool = True,
    lowercase: bool = True,
    numbers: bool = True,
    special_characters: bool = True,
) -> str:

    if not isinstance(length, int) or length < MIN_PASSWORD_LENGTH:
        raise ValueError(
            f"Password length must be an integer of at least {MIN_PASSWORD_LENGTH} characters."
        )
    
    selected_pools = []
    if uppercase:
        selected_pools.append(UPPERCASE_CHARS)
    if lowercase:
        selected_pools.append(LOWERCASE_CHARS)
    if numbers:
        selected_pools.append(DIGIT_CHARS)
    if special_characters:
        selected_pools.append(SPECIAL_CHARS)

    if not selected_pools:
        raise ValueError("At least one character type must be selected.")


    password_chars = [secrets.choice(pool) for pool in selected_pools]


    combined_pool = "".join(selected_pools)
    remaining_length = length - len(password_chars)
    password_chars.extend(secrets.choice(combined_pool) for _ in range(remaining_length))
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def check_password_strength(password: str):

    if not password:
        return "Very Weak", 0, ["Password cannot be empty."]

    score = 0
    suggestions = []
    length = len(password)
    
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if length < 8:
        suggestions.append("Use at least 8 characters (12+ recommended).")
    elif length < 12:
        suggestions.append("Use at least 12 characters.")

    has_lower = bool(re.search(r"[a-z]", password))
    if has_lower:
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    has_upper = bool(re.search(r"[A-Z]", password))
    if has_upper:
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    has_digit = bool(re.search(r"\d", password))
    if has_digit:
        score += 1
    else:
        suggestions.append("Add numbers.")

    has_special = bool(re.search(rf"[{re.escape(SPECIAL_CHARS)}]", password))
    if has_special:
        score += 1
    else:
        suggestions.append("Add special characters.")

    if has_lower and has_upper and has_digit and has_special:
        score += 1

    if length >= 20:
        score += 1

    is_common_weak = password.lower() in COMMON_WEAK_PASSWORDS
    if is_common_weak:
        score = 0
        suggestions.insert(
            0, "Warning: This is a commonly used weak password and is unsafe."
        )

    if re.search(r"(.)\1{2,}", password):
        score -= 1
        suggestions.append("Avoid repeated characters (e.g., 'aaa', '111').")

    matched_sequences = [seq for seq in SEQUENTIAL_NUMBER_PATTERNS if seq in password]
    if matched_sequences:
        score -= 1
        suggestions.append(f"Avoid sequential numbers (e.g., '{matched_sequences[0]}').")

    score = max(0, score)
    if is_common_weak:
        score = 0

    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    elif score == 7:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, score, suggestions

def get_yes_no_input(prompt: str) -> bool:

    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def get_integer_input(prompt: str, min_value: int) -> int:

    while True:
        raw_input = input(prompt).strip()
        try:
            value = int(raw_input)
            if value < min_value:
                print(f"Password length must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

def handle_generate_password() -> None:

    print("\n" + "=" * 50)
    print("GENERATE PASSWORD")
    print("=" * 50)

    length = get_integer_input(
        f"Password length (minimum {MIN_PASSWORD_LENGTH}): ", MIN_PASSWORD_LENGTH
    )

    while True:
        include_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
        include_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
        include_numbers = get_yes_no_input("Include numbers? (y/n): ")
        include_special = get_yes_no_input("Include special characters? (y/n): ")

        if any([include_upper, include_lower, include_numbers, include_special]):
            break
        print("\nError: You must select at least one character type! Please try again.\n")

    try:
        password = generate_password(
            length=length,
            uppercase=include_upper,
            lowercase=include_lower,
            numbers=include_numbers,
            special_characters=include_special,
        )
        strength, score, _ = check_password_strength(password)

        print("\n" + "=" * 50)
        print("Generated Password:")
        print(password)
        print("=" * 16)
        print(f"\nStrength: {strength}")
        print(f"Score: {score}")
    except ValueError as err:
        print(f"\nError generating password: {err}")


def handle_check_password() -> None:

    print("\n" + "=" * 50)
    print("CHECK PASSWORD STRENGTH")
    print("=" * 50)

    password = input("Enter password to check: ")

    if not password:
        print("\nError: Password cannot be empty.")
        return

    strength, score, suggestions = check_password_strength(password)

    print("\n" + "=" * 50)
    print("Password Strength Result")
    print("=" * 24)
    print(f"\nPassword : {password}")
    print(f"Strength : {strength}")
    print(f"Score    : {score}")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"• {suggestion}")
    else:
        print("\nExcellent password!")

def main() -> None:

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    while True:
        print("\n" + "=" * 50)
        print("PASSWORD GENERATOR & STRENGTH CHECKER")
        print("=" * 37)
        print("\nChoose an option:")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        try:
            choice = input("\nEnter your choice (1-3): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting application. Goodbye!")
            sys.exit(0)

        if choice == "1":
            try:
                handle_generate_password()
            except (KeyboardInterrupt, EOFError):
                print("\n\nOperation cancelled. Returning to main menu.")
        elif choice == "2":
            try:
                handle_check_password()
            except (KeyboardInterrupt, EOFError):
                print("\n\nOperation cancelled. Returning to main menu.")
        elif choice == "3":
            print("\nThank you for using Password Generator & Strength Checker. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()













    