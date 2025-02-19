from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("\nCOFFEE MACHINE\n")

is_machine_on = True

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


while is_machine_on:
	order = input(f"What would you like? {menu.get_items()}: ").lower()

	match order:
		case "report":
			coffee_machine.report()
			money_machine.report()
		case 'off':
			is_machine_on = False
		case _:
			drink = menu.find_drink(order)
			if drink != None:
				money_machine.make_payment(drink.cost)
				coffee_machine.make_coffee(drink)
	