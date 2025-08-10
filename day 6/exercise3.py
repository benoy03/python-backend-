# Exercise 3: User Registration with Custom Exceptions

# --- Custom Exception Definitions ---
class InvalidLengthError(Exception):
    """Raised when the username length is not within the valid range."""
    pass

class InvalidCharacterError(Exception):
    """Raised when the username contains non-alphanumeric characters."""
    pass

def register_user():
    """
    Prompts for a username, validates it with custom exceptions, and writes valid
    usernames to a file.
    """
    username = input("Enter a new username: ")
    registration_successful = False

    try:
        # Step 1: Validate username length
        if not 5 <= len(username) <= 15:
            raise InvalidLengthError("Username must be between 5 and 15 characters long.")

        # Step 2: Validate username characters
        if not username.isalnum():
            raise InvalidCharacterError("Username must contain only alphanumeric characters.")

        # Step 3: Write valid username to file
        with open("users.txt", "a") as user_file:
            user_file.write(f"{username}\n")
        
        print(f"Username '{username}' successfully registered.")
        registration_successful = True

    except (InvalidLengthError, InvalidCharacterError) as e:
        print(f"Registration failed: {e}")
    except IOError as e:
        print(f"File error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # The finally block always executes, regardless of whether an exception occurred
        status = "successful" if registration_successful else "failed"
        print(f"Registration attempt for '{username}' has {status}.")

# Run the program
register_user()

