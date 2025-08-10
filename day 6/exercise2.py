# Exercise 2: Temperature Converter with Formatted Output

# --- Setup: Create a dummy input file for demonstration ---
try:
    with open("celsius.txt", "w") as f:
        f.write("0\n")
        f.write("25\n")
        f.write("100\n")
        f.write("-40\n")
        f.write("abc\n") # This line will cause a ValueError
except IOError as e:
    print(f"Error creating dummy file: {e}")
    exit()

def convert_temperatures(input_file, output_file):
    """
    Reads Celsius temperatures from a file, converts them to Fahrenheit,
    and writes the formatted results to another file.
    """
    try:
        # Open the input file for reading and the output file for writing
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                celsius_str = line.strip()
                try:
                    # Attempt to convert the string to a floating-point number
                    celsius_temp = float(celsius_str)
                    
                    # Convert to Fahrenheit: F = (C * 9/5) + 32
                    fahrenheit_temp = (celsius_temp * 9/5) + 32
                    
                    # Write the formatted output using an f-string
                    outfile.write(f"{celsius_temp:.2f}C = {fahrenheit_temp:.2f}F\n")
                
                except ValueError:
                    # Handle case where the line is not a valid number
                    print(f"Skipping invalid data: '{celsius_str}' is not a number.")

        print(f"Temperature conversion complete. Results saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
convert_temperatures("celsius.txt", "fahrenheit.txt")
