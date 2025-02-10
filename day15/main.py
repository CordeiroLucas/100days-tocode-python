from CoffeeMachine import *

machine = CoffeeMachine(300, 200, 100)

print("\n--------------------")
machine.report()
print("\n--------------------\n")
machine.buy('latte', 4.92)
print("\n--------------------")
machine.report()
print("\n--------------------\n")
machine.isResourcesSufficient('cappuccino')
print("\n--------------------\n")
machine.buy('expresso', 0.41)
print("\n--------------------\n")
machine.buy('expresso', 3.64)

