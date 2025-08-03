def fibonacci(n):
    """
    Function to generate Fibonacci series up to the nth term using a loop.

    Parameters:
    n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    list: A list containing the Fibonacci series.
    """
    fib_series = [0, 1]  

    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series


num_terms = int(input("Enter the number of terms for Fibonacci series: "))
print(fibonacci(num_terms))
