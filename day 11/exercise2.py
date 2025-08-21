import re

def extract_dates(text):
    """
    Finds dates in DD-MM-YYYY or DD/MM/YYYY format.
    Returns a list of matching dates.
    """
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)


sample_text = "Alice was born on 12-05-1990, Bob on 23/11/1985, Carol on 01-01-2000."
dates = extract_dates(sample_text)
print(dates)
