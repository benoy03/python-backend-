import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"[TIMER] {func.__name__} executed in {elapsed:.4f} seconds")
        
        
        with open("execution_log.txt", "a") as f:
            f.write(f"{func.__name__} took {elapsed:.4f} seconds\n")
        
        return result
    return wrapper


@measure_time
def process_data(n):
   
    total = 0
    for i in range(n):
        total += i ** 2
    return total


# Test
print(process_data(1000000))
print("Execution time logged in execution_log.txt ✅")
