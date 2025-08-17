def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function '{func.__name__}' has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0  # Initialize counter
    return wrapper


@call_counter
def greet(name):
    return f"Hello, {name}!"


# Test
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

print("Total calls:", greet.calls)
