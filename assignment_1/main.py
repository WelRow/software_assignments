import sandwhichMachine
from data import recipes, resources
import cashier

receipe = recipes
resources = resources

sm1 = sandwhichMachine.SandwichMachine(resources, receipe)
cashier1 = cashier.Cashier(receipe)

isOn = True

while isOn:
    input1 = input("What would you like? (small/ medium/ large/ off/ report): ")

    if input1 == "off":
        isOn = False
    
    elif input1 == "report":
        print(f"Bread: {resources['bread']} slice(s)\nHam: {resources['ham']} slice(s)\nCheese: {resources['cheese']} pound(s)")

    elif input1 == "small":
        if sm1.check_resources("small") and cashier1.transaction_result(cashier1.process_coins(), "small"):
            sm1.make_sandwich("small", receipe["small"]["ingredients"])
    
    elif input1 == "medium":
        if sm1.check_resources("medium") and cashier1.transaction_result(cashier1.process_coins(), "medium"):
            sm1.make_sandwich("medium", receipe["medium"]["ingredients"])

    elif input1 == "large":
        if sm1.check_resources("large") and cashier1.transaction_result(cashier1.process_coins(), "large"):
            sm1.make_sandwich("large", receipe["large"]["ingredients"])
