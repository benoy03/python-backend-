from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):
    """
    Converts time string from one timezone to another.
    time_str format: 'YYYY-MM-DD HH:MM:SS'
    """
    naive_dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    
    localized_dt = from_zone.localize(naive_dt)
    converted_dt = localized_dt.astimezone(to_zone)
    return converted_dt.strftime("%Y-%m-%d %H:%M:%S")

time_original = "2023-10-05 14:30:00"
converted_time = convert_timezone(time_original, "US/Eastern", "UTC")
print(f"{time_original} US/Eastern --> {converted_time} UTC")
