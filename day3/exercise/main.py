import statistics_calculator
import temperature_utils

def get_numbers_from_user():
    while True:
        user_input = input("Enter a list of numbers separated by commas (e.g., 1, 2, 3): ")
        try:
            numbers = [float(num.strip()) for num in user_input.split(',')]
            return numbers
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by commas.")

def temperature_conversion_menu():
    while True:
        choice = input("\nChoose conversion:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n3. Exit\nEnter choice (1/2/3): ")
        if choice == "1":
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = temperature_utils.fahrenheit_to_celsius(f)
                print(f"{f}°F = {c:.2f}°C")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = temperature_utils.celsius_to_fahrenheit(c)
                print(f"{c}°C = {f:.2f}°F")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            print("Exiting temperature conversion.")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Calculate Statistics")
        print("2. Temperature Conversion")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            while True:
                numbers = get_numbers_from_user()
                if len(numbers) < 2:
                    print("Please enter at least two numbers to calculate statistics.\n")
                else:
                    break
            stats = statistics_calculator.calculate_statistics(numbers)
            print(f"\nStatistics for the list: {numbers}")
            print(f"Mean: {stats['mean']}")
            print(f"Median: {stats['median']}")
            print(f"Variance: {stats['variance']}")
            print(f"Standard Deviation: {stats['standard_deviation']}")
        
        elif choice == "2":
            temperature_conversion_menu()
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
