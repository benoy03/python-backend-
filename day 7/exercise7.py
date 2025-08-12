class MenuItem:
    """A class to represent a menu item."""
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        """Returns a formatted string of the menu item details."""
        return f"{self.name} ({self.category}): ${self.price:.2f}"

class Order:
    """A class to manage a restaurant order."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Adds a MenuItem object to the order."""
        self.items.append(item)
        print(f"Added '{item.name}' to the order.")

    def remove_item(self, name):
        """Removes a menu item from the order by its name."""
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Removed '{item.name}' from the order.")
                return
        print(f"Item '{name}' not found in order.")

    def calculate_total(self):
        """Calculates the total price of all items in the order."""
        return sum(item.price for item in self.items)

    def display_order(self):
        """Prints a detailed list of all items and the total price."""
        if not self.items:
            print("The order is empty.")
            return

        print("\n--- Current Order ---")
        for item in self.items:
            print(f"- {item.name}: ${item.price:.2f}")
        total = self.calculate_total()
        print(f"---------------------")
        print(f"Total: ${total:.2f}")


print("\n--- Exercise 7: Restaurant Order System with User Input ---")
menu = {
    "burger": MenuItem("Burger", 8.50, "Main Course"),
    "fries": MenuItem("Fries", 3.00, "Side"),
    "soda": MenuItem("Soda", 2.50, "Drink"),
    "salad": MenuItem("Salad", 6.00, "Appetizer"),
}

my_order = Order()

while True:
    print("\n--- Restaurant Menu ---")
    print("Available Items:")
    for name, item in menu.items():
        print(f" - {item.display()}")
    
    print("\nWhat would you like to do?")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View order")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter the name of the item to add: ").lower()
        if item_name in menu:
            my_order.add_item(menu[item_name])
        else:
            print("That item is not on the menu.")
    elif choice == '2':
        item_name = input("Enter the name of the item to remove: ")
        my_order.remove_item(item_name)
    elif choice == '3':
        my_order.display_order()
    elif choice == '4':
        print("Thank you for your order! Goodbye.")
        break
    else:
        print("Invalid choice.")