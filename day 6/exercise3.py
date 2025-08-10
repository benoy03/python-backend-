
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
       
        if not 5 <= len(username) <= 15:
            raise InvalidLengthError("Username must be between 5 and 15 characters long.")

       
        if not username.isalnum():
            raise InvalidCharacterError("Username must contain only alphanumeric characters.")

       
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
    
        status = "successful" if registration_successful else "failed"
        print(f"Registration attempt for '{username}' has {status}.")


register_user()

