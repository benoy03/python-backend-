import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 29],
    "Salary": [50000, 60000, 75000, 80000, 55000]
}

df = pd.DataFrame(data)

print("=== Dataset ===")
print(df, "\n")


print("=== Summary Statistics ===")
print(df.describe(), "\n")


print("=== Employees with Salary > 60,000 ===")
print(df[df["Salary"] > 60000], "\n")

print(f"Average Age: {df['Age'].mean():.2f}")
