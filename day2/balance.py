class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Invalid amount or insufficient balance")

    def display_balance(self):
        print("Current balance:", self.__balance)


# Main program
account = BankAccount(5000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(1000)
account.display_balance()