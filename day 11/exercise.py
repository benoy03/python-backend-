import re
from datetime import datetime
import pytz


def validate_email(email):
    """
    Validates email using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


emails = [
    "alice@example.com",
    "bob.smith@domain.co.uk",
    "invalid-email@",
    "user@website"
]

print("Email Validation Results:")
for email in emails:
    if validate_email(email):
        print(f"{email} --> Valid")
    else:
        print(f"{email} --> Invalid")

print("\n" + "-"*40 + "\n")


timezones = ["UTC", "US/Eastern", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]

print("Current Time in Different Timezones:")
for tz in timezones:
    tz_obj = pytz.timezone(tz)
    current_time = datetime.now(tz_obj)
    print(f"{tz}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
