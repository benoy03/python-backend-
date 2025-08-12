class BankAccount:
    """A class to model a bank account with deposit/withdraw validation."""
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws from the account if funds are sufficient and amount is positive."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance:.2f}.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")

    def get_balance(self):
        """Returns the current balance."""
        return self.balance


print("\n--- Exercise 3: Bank Account with User Input ---")
account_holder_name = input("Enter account holder's name: ")
account = BankAccount(account_holder_name)

while True:
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        try:
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '2':
        try:
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '3':
        print(f"Current balance for {account.account_holder}: ${account.get_balance():.2f}")
    elif choice == '4':
        print("Exiting bank account system.")
        break
    else:
        print("Invalid choice.")
print("-" * 25)