def validate_positive(func):
    def wrapper(*args, **kwargs):
        
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Invalid input: {arg}. Only positive numbers allowed.")
        for kwarg in kwargs.values():
            if not isinstance(kwarg, (int, float)) or kwarg <= 0:
                raise ValueError(f"Invalid input: {kwarg}. Only positive numbers allowed.")
        return func(*args, **kwargs)
    return wrapper


@validate_positive
def add(a, b):
    return a + b



print(add(5, 10))   

