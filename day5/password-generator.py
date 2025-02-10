# Range, Loops, Random, List

import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '/', '?']

print("Welcome to the PyPassword_listpassword_list Generator!")
total_letters = int(input("How many letters would you like in your password_list?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers? would you like?\n"))

total_pass_size = total_letters+total_symbols+total_numbers

password_list = []

for char in range(0,total_letters):
    random_char = chr(random.randint(97, 122))
    if random.randint(0,1):
        random_char = random_char.upper()
    password_list.append(random_char)
    
for char in range(0,total_numbers):
    password_list.append(random.choice(numbers))

for char in range(0,total_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: ", password)