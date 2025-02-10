# Control Flow and Logical Operators
SMALL =  15.00
MEDIUM = 20.00
LARGE = 25.00

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0.0

match size.upper():
    case 'S':
        bill+=SMALL
    case 'M':
        bill+=MEDIUM
    case 'L':
        bill+=LARGE
        
if pepperoni.upper() == 'Y': 
    if size == 'M' or size == 'L':
        bill+=1
    bill+=2

if extra_cheese.upper() == 'Y':
    bill+=1

print(f"Your final bill is: ${bill}.")