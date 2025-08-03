
import math
import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_variance(numbers):
    return statistics.variance(numbers)

def calculate_standard_deviation(numbers):
    return statistics.stdev(numbers)

def calculate_statistics(numbers):
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    variance = calculate_variance(numbers)
    std_dev = calculate_standard_deviation(numbers)
    
    return {
        "mean": mean,
        "median": median,
        "variance": variance,
        "standard_deviation": std_dev
    }
