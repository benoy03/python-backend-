import re
from datetime import datetime

def parse_log_timestamps(log):
    """
    Extracts timestamps from logs in format:
    [DD/Mon/YYYY:HH:MM:SS +0000]
    Converts to 'YYYY-MM-DD HH:MM:SS'.
    """
    pattern = r'\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\]'
    matches = re.findall(pattern, log)
    
    converted = []
    for ts in matches:
        dt = datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S")
        converted.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
    return converted

log_sample = "[21/Aug/2025:10:25:43 +0000] User logged in\n[21/Aug/2025:11:05:12 +0000] User logged out"
parsed_times = parse_log_timestamps(log_sample)
print(parsed_times)
