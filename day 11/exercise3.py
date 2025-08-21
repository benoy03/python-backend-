from datetime import datetime

def time_until_birthday(birthdate_str):
    """
    Calculates days, hours, minutes until next birthday.
    Input format: YYYY-MM-DD
    """
    today = datetime.now()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    next_birthday = birthdate.replace(year=today.year)
    
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    delta = next_birthday - today
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return days, hours, minutes


birthdate_input = "1990-08-25"
days, hours, minutes = time_until_birthday(birthdate_input)
print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes")
