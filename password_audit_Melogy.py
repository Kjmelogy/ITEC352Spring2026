"""Password Strength Audit starter template.

Complete each TODO. Do not change the required function names or parameters.
"""


def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""

    # Keep asking until the user enters a valid number
    while True:
        try:
            # Ask the user how many passwords they want to check
            count = int(input("Enter the number of passwords: "))

            # Make sure the number is greater than zero
            if count > 0:
                return count

            print("Please enter a number greater than zero.")

        # Handles input that cannot be converted into a whole number
        except ValueError:
            print("Please enter a valid whole number.")


def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""

    # Keep track of which password requirements are met
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    # Check each character in the password
    for character in password:

        # Check for an uppercase letter
        if character.isupper():
            has_uppercase = True

        # Check for a lowercase letter
        elif character.islower():
            has_lowercase = True

        # Check for a number
        elif character.isdigit():
            has_digit = True

        # Anything else counts as a special character
        else:
            has_special = True

    # Count how many password requirements were met
    requirements_met = sum(
        [has_uppercase, has_lowercase, has_digit, has_special]
    )

    # Determine the password strength
    if requirements_met == 4:
        return "Strong"
    elif requirements_met >= 2:
        return "Moderate"
    else:
        return "Weak"


def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""

    # Display the final password results
    print("\nPassword Strength Summary")
    print(f"Strong: {strong_count}")
    print(f"Moderate: {moderate_count}")
    print(f"Weak: {weak_count}")


def main():
    """Coordinate the password audit."""

    # Start the password strength counters at zero
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    # Get the number of passwords from the user
    password_count = get_password_count()

    # Repeat for the number of passwords entered
    for _ in range(password_count):

        # Ask the user for a password
        password = input("Enter a password: ")

        # Send the password to the function and get its rating
        rating = evaluate_password(password)

        # Add one to the correct password strength category
        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

    # Show the final results
    display_summary(strong_count, moderate_count, weak_count)


# Start the program by calling the main function
if __name__ == "__main__":
    main()
