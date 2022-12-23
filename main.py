from data import MENU
from data import resources

# Coffee machine is on
is_on = True

# While coffee machine is on
while is_on:
    # Prompt user for which coffee they would like
    choice = (input("What would you like to purchase? (espresso/latte/cappuccino): ")).lower()
    # Secret response to turn off the coffee machine
    if choice == "off":
        is_on = False
    # Secret response to print out a report of the currently available resources
    elif choice == "report":
        print(f"""
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${resources["money"]}
        """)
    # Available coffee choices
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        coffee = MENU[choice]
        ingredients = coffee["ingredients"]
        price_of_coffee = round(coffee['cost'], 2)
        enough_resources = True
        # Check to see if there are enough ingredients for the selected coffee
        for item in ingredients:
            if ingredients[item] > resources[item]:
                enough_resources = False
                print(f"Sorry, there is not enough {item}.")
        if not enough_resources:
            continue
        # Prompt user to insert coins to pay for the coffee
        print(f"A {choice} costs ${format(price_of_coffee, '.2f')}. "
              f"Please insert the appropriate amount of coins.")
        total = int(input("How many quarters would you like to insert? ")) * 0.25
        total += int(input("How many dimes would you like to insert? ")) * 0.1
        total += int(input("How many nickles would you like to insert? ")) * 0.05
        total += int(input("How many pennies would you like to insert? ")) * 0.01
        # Check if amount entered is enough to purchase the chosen coffee
        if total < price_of_coffee:
            print("Sorry, that is not enough money. Money refunded.")
            continue
        elif total > price_of_coffee:
            change = round(total - price_of_coffee, 2)
            print(f"You get ${format(change, '.2f')} back in change.")
        # Add money to resources
        resources["money"] += price_of_coffee
        # Make the coffee
        for item in ingredients:
            resources[item] -= ingredients[item]
        print(f"Here is your {choice}. Enjoy!")
    # If anything else was entered
    else:
        print("Invalid choice")
