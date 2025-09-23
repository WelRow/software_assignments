
class SandwichMachine:
    def __init__(self, machine_resources, receipes):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        
        self.machine_resources = machine_resources
        self.receipes = receipes

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Assuming ingredients = size of sandwhich cus it doesnt make any sense if it isnt

        self.sandwhichIngredients = self.receipes[ingredients]["ingredients"]

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]

        print(f"{sandwich_size} sandwhich is ready. Bon appetit!")
                    

### Make an instance of SandwichMachine class and write the rest of the codes ###


