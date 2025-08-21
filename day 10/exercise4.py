

def extract_vowels(s):
    vowels = "aeiou"
    return {ch.upper() for ch in s if ch.lower() in vowels}


s = "Hello World"
print(extract_vowels(s)) 
