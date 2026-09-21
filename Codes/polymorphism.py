class BankAccount:
    def withdraw(self):
        print("Money WIthdrawn!")

class SavingsAccount(BankAccount) :
    def withdraw(self):     # Method Overriding
        print("Money withdrawn from Savings Account!")

sa = SavingsAccount()
sa.withdraw()