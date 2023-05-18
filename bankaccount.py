class BankAccount:
    x = "balance"

    def deposit(self):
        print("Deposit")

    def withdraw(self):
        print("withdraw")

    def checkBalance(self):
        print("checkBalance")

    def transfer(self):
        print("transfer")

class InterestAccount(BankAccount):
    def interest(self):
        print("interest")

    def deposit(self):
        print("Deposit")

class ChargingAccount(BankAccount):
    def fee(self):
        print("fee")

inter = InterestAccount()
inter.deposit()
inter.withdraw()
inter.checkBalance()
inter.transfer()

y = inter.x
print(y)

char = ChargingAccount()
char.deposit()
char.withdraw()
char.checkBalance()
char.transfer()

z = char.x
print(z)