class BankAccount:
    def withdraw(self):
        print("Money withdrawn!")

class SavingsAccount(BankAccount) :
    pass

class CurrentAccount(BankAccount) :
    pass

sa = SavingsAccount()
sa.withdraw()

ca = CurrentAccount()
ca.withdraw()



