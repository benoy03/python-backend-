
raw_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, raw_input.strip().split()))


sorted_numbers = sorted(numbers)
print("Sorted:", sorted_numbers)


even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)


squares = [x ** 2 for x in numbers]
print("Squares:", squares)


coordinates = (10, 20)
x, y = coordinates
print(f"Tuple: {coordinates}")
print(f"Unpacked -> x: {x}, y: {y}")
