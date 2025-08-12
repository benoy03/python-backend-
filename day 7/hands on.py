
class BankAccount:
    """A class to model a simple bank account."""

    def __init__(self, owner_name, initial_balance=0.0):
       
        self.owner_name = owner_name
        self.balance = initial_balance


    def deposit(self, amount):
        """Adds a specified amount to the account balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        """Subtracts a specified amount from the account, if funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Withdrawal failed. Insufficient funds. Current balance: ${self.balance:.2f}.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")

  
    def display_info(self):
        """Prints the owner's name and current balance."""
        print("-----------------------------------")
        print(f"Account Owner: {self.owner_name}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-----------------------------------")




if __name__ == '__main__':

    owner_name = input("Enter the account owner's name: ")
    while True:
        try:
            initial_balance_input = input("Enter the initial balance: $")
            initial_balance = float(initial_balance_input)
            if initial_balance >= 0:
                break
            else:
                print("Initial balance cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number for the balance.")

    user_account = BankAccount(owner_name, initial_balance)
    print("\nAccount created successfully!")
    user_account.display_info()


    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: $"))
                user_account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                user_account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '3':
            user_account.display_info()

        elif choice == '4':
            print("Thank you for using the bank account system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
