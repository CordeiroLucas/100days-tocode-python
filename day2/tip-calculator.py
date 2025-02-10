# Math, Data Types, String Format

print("Welcome to the tip calculator!")

totalBill =  float(input("What was the total bill? $"))
tipPercentage = int(input("How much tipo would you like to give? 10, 12, or 15? "))/100
peopleNumber = int(input("How many people to split the bill? "))

payment = (totalBill+totalBill*tipPercentage)/peopleNumber

print(f"Each person should pay: {payment}")