import re

def validate_email(email):
    """
    Validates email address:
    username@domain.extension
    username: letters, numbers, ., _, -
    domain: letters, numbers, -
    extension: 2-4 letters
    """
    pattern = r'^[\w.-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$'
    return bool(re.match(pattern, email))


emails = ["alice@example.com", "bob.smith@domain.co.uk", "invalid-email@", "user@website"]
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
