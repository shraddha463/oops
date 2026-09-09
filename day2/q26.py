class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


# Create object
account1 = BankAccount("Shraddha", 25000)

# Display balance
account1.display_balance()