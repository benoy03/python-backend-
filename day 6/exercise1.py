
try:
    with open("input_words.txt", "w") as f:
        f.write("Radar\n")
        f.write("python\n")
        f.write("Madam\n")
        f.write("level\n")
        f.write("hello\n")
        f.write("Civic\n")
    print("Created 'input_words.txt' with sample data.")
except IOError as e:
    print(f"Error creating dummy file: {e}")

    exit()

def find_palindromes(input_file, output_file):
    """
    Reads words from an input file, checks for palindromes, and writes them to an output file.
    
    Args:
        input_file (str): The name of the file to read from.
        output_file (str): The name of the file to write palindromes to.
    """
    try:
        
        with open(input_file, 'r') as infile:
            words = [line.strip() for line in infile.readlines()]

        palindromes = []
       
        for word in words:
      
            if word and word.lower() == word[::-1].lower():
                palindromes.append(word.upper())
        
      
        with open(output_file, 'w') as outfile:
            for palindrome in palindromes:
                outfile.write(f"{palindrome}\n")

        print(f"Successfully found {len(palindromes)} palindromes and wrote them to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
find_palindromes("input_words.txt", "palindromes.txt")
