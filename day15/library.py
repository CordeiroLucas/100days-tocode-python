class CoffeeMachine:
    MENU = {
        'expresso':{
            'ingredients': {
                'water':50,
                'coffee':18,
            },
            'cost':1.5,
        },

        'latte':{
            'ingredients':{
                'water':200,
                'coffee':24,
                'milk':150,
            },
            'cost':2.5,
        },

        'cappuccino':{
            'ingredients':{
                'water':250,
                'coffee':24,
                'milk':100,
            },
            'cost':3.0,
        }
    }
    UNITS = {
        'water':'ml',
        'milk':'ml',
        'coffee':'g',
        'money':'$',
    }
    resources:dict
    total_cups:int
    balance:float

    def __init__(self, water, milk, coffee):
        self.resources = {
            'water':water,
            'milk':milk,
            'coffee':coffee,
        }
        self.total_cups = 0
        self.balance = 0
    
    def __make__(self, coffee:str):
        asked_coffee = self.MENU[coffee]
        for ingredient in asked_coffee['ingredients']:
            self.resources[ingredient] -= asked_coffee['ingredients'][ingredient]
        print(f"Here is your {coffee} ☕ Enjoy!")
    
    def __getPayment__(self, coffee:str, payment:float):
        asked_coffee = self.MENU[coffee]
         
        if payment >= asked_coffee['cost']:
            if payment > asked_coffee['cost']:
                change = payment - asked_coffee['cost']
                print(f"Here is ${change} in change!")
            self.balance += asked_coffee['cost']
            return True
        
        else:
            print(f"Sorry that's not enough money. Money refunded.")
            return False

    def isResourcesSufficient(self, coffee:str):
        asked_coffee = self.MENU[coffee]

        for ingredient in asked_coffee['ingredients']:
            if asked_coffee['ingredients'][ingredient] > self.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def buy(self, coffee:str, payment:float):
        if self.__getPayment__(coffee, payment) and self.isResourcesSufficient(coffee):
            self.__make__(coffee)
            self.total_cups += 1

    def report(self):
        print("Machine Report:\n")
        for rsc in self.resources:
            print(f"{rsc.capitalize()}: {self.resources[rsc]}{self.UNITS[rsc]}")
        print(f"Money: {self.UNITS['money']}{self.balance}")
        print(f"Total Cups Made: {self.total_cups}")
    
    def refill(self, water:int, milk:int, coffee:int):
        self.resources['water'] += water
        self.resources['milk'] += milk
        self.resources['coffee'] += coffee
        
        print("Refilled, now:\n")
        self.report()
    
def coin_counter(quarter, dime, nickel, penny):
    total_balance = 0
    total_balance += quarter*0.25
    total_balance += dime*0.1
    total_balance += nickel*0.05
    total_balance += penny*0.01
    return total_balance
    