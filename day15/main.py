from library import *

coins = {
    'quarters':0.25,
    'dimes':0.1,
    'nickels':0.05,
    'pennies':0.01,
}

machine = CoffeeMachine(300, 200, 100)

print("COFFEE MACHINE\n")

is_machine_ON = True

while is_machine_ON:
    option = input("What would you like? (expresso/latte/cappuccino): ").lower()

    match option:
        case 'report':
            machine.report()
        case 'refill':
            machine.refill(300,200,100)
        case 'off':
            is_machine_ON = False
        case _:
            try:
                if machine.isResourcesSufficient(option):
                    quarters = float(input("How Many Quartes?: "))
                    dimes = float(input("How Many Dimes?: "))
                    nickels = float(input("How Many Nickels?: "))
                    pennies = float(input("How Many Pennies?: "))

                    machine.buy(option, coin_counter(quarters, dimes, nickels, pennies))
            except KeyError:
                print("Invalid Option!")