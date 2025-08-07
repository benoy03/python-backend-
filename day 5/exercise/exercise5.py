
inventory = {
    "apple": {"price": 1.5, "category": "fruit"},
    "banana": {"price": 0.75, "category": "fruit"},
    "milk": {"price": 2.99, "category": "dairy"},
    "bread": {"price": 3.25, "category": "bakery"},
    "cheese": {"price": 4.5, "category": "dairy"},
    "chocolate": {"price": 2.25, "category": "snacks"}
}


cart = {
    "apple": 4,
    "milk": 2,
    "bread": 1,
    "cheese": 1,
    "chocolate": 3
}


total_price = 0
unique_categories = set()
most_expensive_item = ""
max_price = 0

receipt_lines = []

for item, quantity in cart.items():
    
    if (data := inventory.get(item)):
        item_total = data["price"] * quantity
        total_price += item_total

        
        unique_categories.add(data["category"])

        
        if data["price"] > max_price:
            max_price = data["price"]
            most_expensive_item = item

        receipt_lines.append(f"{item.capitalize():<12} x{quantity:<2} @ ${data['price']:.2f} = ${item_total:.2f}")


print("\n🧾 RECEIPT")
print("-" * 35)
for line in receipt_lines:
    print(line)
print("-" * 35)
print(f"Total Price:       ${total_price:.2f}")
print(f"Unique Categories: {', '.join(sorted(unique_categories))}")
print(f"Most Expensive:    {most_expensive_item.capitalize()} (${max_price:.2f})")
