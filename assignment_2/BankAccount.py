
class BankAccount():
    bankTitle = "KanyindaBank"

    def __init__(self, customerName, currentBalance):
        self.customerName = customerName
        self.currentBalance = currentBalance
        self.minimumBalance = 25
    
    def deposit(self, amount):
        self.currentBalance += amount
    
    def withdraw(self, amount):
        if (self.currentBalance < self.minimumBalance):
            print("You cannot withdraw as your current balance below you're account minimum!")
    
    def __str__(self):
        return f"{self.customerName} {self.currentBalance} {BankAccount.bankTitle}"

p1 = BankAccount("Josias Kanyinda", 100000000)
p2 = BankAccount("Trump", 0)

print(p1)