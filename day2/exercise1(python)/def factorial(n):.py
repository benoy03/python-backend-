def factorial(n):
    """
    Function to find the factorial of a number using recursion.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the number.
    """
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  


num = int(input("Enter a number to find its factorial: "))
print(factorial(num))
