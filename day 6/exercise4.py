# Exercise 4: Log File Analyzer

# --- Setup: Create a dummy log file for demonstration ---
try:
    with open("server.log", "w") as f:
        f.write("192.168.1.1 200 /index.html\n")
        f.write("10.0.0.5 404 /login\n")
        f.write("192.168.1.10 500 /api/data\n")
        f.write("10.0.0.5 200 /images/logo.png\n")
        f.write("192.168.1.1 200 /about.html\n")
        f.write("malformed line\n") # This line will be ignored
        f.write("10.0.0.5 404 /contact\n")
    print("Created 'server.log' with sample data.")
except IOError as e:
    print(f"Error creating dummy file: {e}")
    exit()

def analyze_log_file(input_file, output_file):
    """
    Analyzes a log file to count HTTP status codes and writes a summary report.
    """
    status_counts = {200: 0, 404: 0, 500: 0}
    
    try:
        with open(input_file, 'r') as logfile:
            for line in logfile:
                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        status_code = int(parts[1])
                        if status_code in status_counts:
                            status_counts[status_code] += 1
                    except (ValueError, IndexError):
                        # Handle malformed lines where the status code is not a number
                        pass

        # Write the summary report to the output file
        with open(output_file, 'w') as report_file:
            report_file.write("Server Log Analysis Report\n\n")
            report_file.write(f"Successful (200): {status_counts.get(200, 0)}\n")
            report_file.write(f"Not Found (404): {status_counts.get(404, 0)}\n")
            report_file.write(f"Server Error (500): {status_counts.get(500, 0)}\n")
        
        print(f"Log analysis complete. Report saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
analyze_log_file("server.log", "report.txt")
