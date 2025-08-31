import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "Age": [25, 30, 35, 40, 29, 33],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 60000, 75000, 80000, 55000, 90000]
}

df = pd.DataFrame(data)


df["Bonus"] = df["Salary"] * 0.1
print("=== DataFrame with Bonus ===")
print(df, "\n")


grouped = df.groupby("Department")[["Salary", "Bonus"]].mean()
print("=== Average Salary and Bonus by Department ===")
print(grouped, "\n")


highest_salary = df.loc[df.groupby("Department")["Salary"].idxmax()]
print("=== Highest Salary in Each Department ===")
print(highest_salary, "\n")


df["AgeGroup"] = pd.cut(df["Age"], bins=[20, 30, 40, 50], labels=["20-30", "31-40", "41-50"])
pivot = df.pivot_table(values="Salary", index="Department", columns="AgeGroup", aggfunc="mean")
print("=== Pivot Table: Average Salary by Department and Age Group ===")
print(pivot)
