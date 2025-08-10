import string

def count_word_frequency(input_filename, output_filename):
    """
    Counts the frequency of each word in an input file and writes the results to an output file.
    
    Args:
        input_filename (str): The path to the input text file.
        output_filename (str): The path to the output file where word counts will be saved.
    """
    word_counts = {}
    
    try:
      
        with open(input_filename, 'r', encoding='utf-8') as infile:
            text = infile.read()

       
        text = text.lower()
        
        text = text.translate(str.maketrans('', '', string.punctuation))
        
      
        words = text.split()

     
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
      
        with open(output_filename, 'w', encoding='utf-8') as outfile:
         
            outfile.write("Word Frequency Counts:\n\n")
            for word, count in sorted(word_counts.items()):
                outfile.write(f"'{word}': {count}\n")
        
        print(f"Successfully counted word frequencies from '{input_filename}' and saved to '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please ensure the file exists in the correct directory.")
    except Exception as e:
        print(f"An unexpected error occurred during file processing: {e}")


with open('sample.txt', 'w') as f:
    f.write("This is a sample text file. This file contains some sample text. We will count the words in this file.")


count_word_frequency('sample.txt', 'word_counts.txt')