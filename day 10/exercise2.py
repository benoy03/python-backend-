

def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield num * sign
        sign *= -1



nums = [1, 2, 3, 4, 5]
print(list(alternating_signs(nums)))  
