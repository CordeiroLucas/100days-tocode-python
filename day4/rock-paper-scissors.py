import random

options = ["rock", "paper", "scissors"]

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
computerChoice = random.randint(0,2)

if playerChoice >= 3 or playerChoice < 0:
    print("Invalid Number. You Lose!")
elif playerChoice == 0 and computerChoice == 2:
    print("You Win")
elif computerChoice == 0 and playerChoice == 2:
    print("You Lose!")
elif computerChoice > playerChoice:
    print("You Lose!")
elif playerChoice > computerChoice:
    print("You Win!")
elif playerChoice == computerChoice:
    print("It's a Draw!")
    
    