

class Cashier:
    def __init__(self, receipes):
        self.receipes = receipes

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        
        cost = self.receipes[cost]["cost"]
        
        if coins - cost < 0:
            print("money is insufficient. ")
            return False
        print (f"Here is ${coins - cost} in change.")
        return True
    
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        
        print("Please insert coins.")
        self.deposit = 0.0
        self.dollars = float(input("how many large dollars?: "))
        self.deposit += self.dollars
        self.halfDollars = float(input("how many half dollars?: "))
        self.deposit += self.halfDollars
        self.quarters = float(input("how many quarters?: "))
        self.deposit += self.quarters
        self.nickels = float(input("how many nickels? "))
        self.deposit += self.nickels

        return self.deposit