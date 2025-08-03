

bill = float(input('whats uer total bill'))
tip_percentage= float(input('What percentage tip would you like to give?'))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
split_amount = total_bill / people

print(f"\nTip Amount: ${tip_amount:.2f}")
print(f"Total Bill with Tip: ${total_bill:.2f}")
print(f"Each Person Should Pay: ${split_amount:.2f}")

