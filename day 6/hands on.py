
def process_file(input_filename, output_filename):
    try:
     
        with open(input_filename, 'r') as infile:
            content = infile.read()
            
       
        processed_content = content.upper()
        
       
        with open(output_filename, 'w') as outfile:
            outfile.write(processed_content)
            
        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


process_file('input.txt', 'output.txt')