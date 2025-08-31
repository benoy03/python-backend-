import pandas as pd
from PIL import Image

# ---------------------------
# 1. DATA ANALYSIS
# ---------------------------

# Example dataset (can be replaced with CSV)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 29],
    "Salary": [50000, 60000, 75000, 80000, 55000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("=== Dataset ===")
print(df, "\n")


print("=== Summary Statistics ===")
print(df.describe(), "\n")


print("=== Employees with Salary > 60,000 ===")
print(df[df["Salary"] > 60000], "\n")


avg_age = df["Age"].mean()
print(f"Average Age: {avg_age:.2f}\n")



image = Image.open("example.jpg")


gray = image.convert("L")

gray.save("output_gray.jpg")

print("✅ Image processing complete! Grayscale image saved as output_gray.jpg")
