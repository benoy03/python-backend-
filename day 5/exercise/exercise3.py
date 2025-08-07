print("\n--- Exercise 3: Walrus Operator ---")

while (num := int(input("3.1 Enter a number greater than 10: "))) <= 10:
    print("Too small, try again.")
print("Accepted number:", num)
