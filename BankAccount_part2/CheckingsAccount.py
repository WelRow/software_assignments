from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customerName, currentBalance=0.0, transferLimit=500.0):
        # Call the constructor of the parent class
        super().__init__(customerName, currentBalance)
        self.transferLimit = transferLimit
        

    def transfer(self, amount, recipientAccount: BankAccount):
        if amount > self.transferLimit:
            print(f"Transfer failed. Amount exceeds the transfer limit of ${self.transferLimit:.2f}.")
        elif 0 < amount <= self.currentBalance:
            self.withdraw(amount)
            recipientAccount.deposit(amount)
            print(f"Successfully transferred ${amount:.2f} to {recipientAccount.customerName}.")
        elif amount > self.currentBalance:
            print("Transfer failed. Insufficient funds.")
        else:
            print("Transfer amount must be positive.")
