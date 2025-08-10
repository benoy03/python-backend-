

import re 


try:
    with open("passwords.txt", "w") as f:
        f.write("MyPassword123\n")
        f.write("weak\n")
        f.write("AnotherStrongPass!\n")
        f.write("short\n")
        f.write("P@ssword123\n")
except IOError as e:
    print(f"Error creating dummy file: {e}")
    exit()

def check_password_strength(password):
    """
    Checks if a password meets the strength requirements.
    Returns True if strong, False otherwise.
    """
    
    if len(password) < 8:
        return False
    
    
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return False
    
   
    if not re.search(r"\d", password):
        return False

   
    if not re.search(r"[!@#$%^&*]", password):
        return False
    
   
    return True

def process_passwords(input_file, output_file):
    """
    Reads passwords from an input file, validates their strength, and
    writes strong passwords to an output file.
    """
    try:
        with open(input_file, 'r') as infile:
            passwords = [line.strip() for line in infile]
        
        strong_passwords = []
        for password in passwords:
            if check_password_strength(password):
                strong_passwords.append(password)
        
        with open(output_file, 'w') as outfile:
            for strong_password in strong_passwords:
                outfile.write(f"{strong_password}\n")

        print(f"Successfully processed passwords. Strong passwords saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


process_passwords("passwords.txt", "strong_passwords.txt")
