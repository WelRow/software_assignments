
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
            return
        print(f"You withdraw ${amount}!")
        self.currentBalance -= amount
    
    def printCustomerInformation(self):
        return f"{self.customerName} {self.currentBalance} {BankAccount.bankTitle}"

if __name__ == "__main__": 

    p1 = BankAccount("Josias Kanyinda", 100000000)
    p2 = BankAccount("Trump", 0)

    print(p2.printCustomerInformation())