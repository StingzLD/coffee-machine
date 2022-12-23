class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        # Prints the current profit
        print(f"Money: {self.CURRENCY}{format(self.profit, '.2f')}")

    def process_coins(self, drink, cost):
        # Returns the total calculated from coins inserted
        print(f"The {drink} costs {self.CURRENCY}{format(cost, '.2f')}.")
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, drink, cost):
        # Returns True when payment is accepted, or False if insufficient
        self.process_coins(drink, cost)
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{format(change, '.2f')} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
