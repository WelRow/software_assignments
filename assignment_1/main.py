import sandwhichMachine
from data import recipes, resources
import cashier

receipe = recipes
resources = resources

sm1 = sandwhichMachine.SandwichMachine(resources, receipe)
cashier1 = cashier.Cashier(receipe)

isOn = True

while isOn:
    userInput = input("What would you like? (small/ medium/ large/ off/ report): ")

    if userInput == "off":
        isOn = False
    
    elif userInput == "report":
        print(f"Bread: {resources['bread']} slice(s)\nHam: {resources['ham']} slice(s)\nCheese: {resources['cheese']} pound(s)")

    elif userInput == "small":
        if sm1.check_resources("small") and cashier1.transaction_result(cashier1.process_coins(), "small"):
            sm1.make_sandwich("small", receipe["small"]["ingredients"])
    
    elif userInput == "medium":
        if sm1.check_resources("medium") and cashier1.transaction_result(cashier1.process_coins(), "medium"):
            sm1.make_sandwich("medium", receipe["medium"]["ingredients"])

    elif userInput == "large":
        if sm1.check_resources("large") and cashier1.transaction_result(cashier1.process_coins(), "large"):
            sm1.make_sandwich("large", receipe["large"]["ingredients"])
