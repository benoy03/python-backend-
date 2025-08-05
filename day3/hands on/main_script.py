
import requests
import my_utilities 

def fetch_and_display_data(url):
    """
    Fetches data from a given URL using the requests library
    and prints the first 500 characters of the content.
    """
    print(f"\n--- Fetching data from: {url} ---")
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print("Successfully fetched data!")
        print("Content snippet (first 500 chars):\n")
        print(response.text[:500])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

if __name__ == "__main__":
    print("--- Using my_utilities module ---")
    name = "Mustafa"
    greeting_message = my_utilities.greet(name)
    print(greeting_message)

    num1 = 10
    num2 = 5
    sum_result = my_utilities.add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")

    product_result = my_utilities.multiply_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is: {product_result}")

    check_even = my_utilities.is_even(num1)
    print(f"Is {num1} even? {check_even}")
    check_even_odd = my_utilities.is_even(num2)
    print(f"Is {num2} even? {check_even_odd}")

    example_url = "https://www.example.com"
    fetch_and_display_data(example_url)
