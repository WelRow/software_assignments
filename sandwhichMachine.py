### Data ###


recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        
        self.machine_resources = machine_resources
        self.isOn = True

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Assuming ingredients = size of sandwhich cus it doesnt make any sense if it isnt

        self.sandwhichIngredients = recipes[ingredients]["ingredients"]

        if self.sandwhichIngredients["bread"] > self.machine_resources["bread"]:
            print("Sorry there is not enough bread.")
            return False
        elif self.sandwhichIngredients["ham"] > self.machine_resources["ham"]:
            print("Sorry there is not enough ham.")
            return False
        elif self.sandwhichIngredients["cheese"] > self.machine_resources["cheese"]:
            print("Sorry there is not enough cheese.")
            return False
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


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        
        cost = recipes[cost]["cost"]
        
        if coins - cost < 0:
            print("money is insufficient. ")
            return False
        print (f"Here is ${coins - cost} in change.")
        return True

        

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]

        print(f"{sandwich_size} sandwhich is ready. Bon appetit!")


    def run(self):
        while self.isOn:
            self.input = input("What would you like? (small/ medium/ large/ off/ report): ")

            if self.input == "off":
                self.isOn = False
            
            elif self.input == "report":
                print(f"Bread: {self.machine_resources['bread']} slice(s)\nHam: {self.machine_resources['ham']} slice(s)\nCheese: {self.machine_resources['cheese']} pound(s)")

            elif self.input == "small":
                if self.check_resources("small") and self.transaction_result(self.process_coins(), "small"):
                    self.make_sandwich("small", recipes["small"]["ingredients"])
            
            elif self.input == "medium":
                if self.check_resources("medium") and self.transaction_result(self.process_coins(), "medium"):
                    self.make_sandwich("medium", recipes["medium"]["ingredients"])

            elif self.input == "large":
                if self.check_resources("large") and self.transaction_result(self.process_coins(), "large"):
                    self.make_sandwich("large", recipes["large"]["ingredients"])
                    

### Make an instance of SandwichMachine class and write the rest of the codes ###

sm1 = SandwichMachine(resources)
sm1.run()
