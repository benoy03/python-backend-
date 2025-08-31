import numpy as np


arr = np.random.randint(1, 101, size=(10, 10))
print("=== Array ===")
print(arr, "\n")


print(f"Mean: {arr.mean():.2f}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {arr.std():.2f}\n")


diagonal = np.diag(arr)
print("=== Main Diagonal ===")
print(diagonal, "\n")


greater_80 = arr[arr > 80]
print("=== Values > 80 ===")
print(greater_80, "\n")


arr[arr < 30] = 0
print("=== Array after replacing values < 30 with 0 ===")
print(arr)
