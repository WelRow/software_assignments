from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customerName, currentBalance=0.0, interestRate=0.02):
        # Call the constructor of the parent class
        super().__init__(customerName, currentBalance)
        self.interestRate = interestRate

    def apply_interest(self):
        interestAmount = self.currentBalance * self.interestRate
        print(f"Applying interest of ${interestAmount:.2f}")
        self.deposit(interestAmount)