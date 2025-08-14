class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Balance: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: ${self.__balance:.2f}"

    def __eq__(self, other):
        return self.account_number == other.account_number


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.get_balance() - amount >= 100:
            super().withdraw(amount)
        else:
            print("Cannot withdraw: Balance would drop below $100.")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft_limit:
            self._Account__balance = self.get_balance() - amount
        else:
            print("Overdraft limit exceeded.")
#str__ → Makes printing an account human-readable.
#eq__ → Compares two accounts by their account_number.