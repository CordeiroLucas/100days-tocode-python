from random import randint

difficulties = {'easy':10, 'hard':5}

number_to_guess = randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number_to_guess}")

sel_difficult = input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()

for n in range(difficulties[sel_difficult]):
    print(f"You have {difficulties[sel_difficult] - n} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
        print("Correct Answer!")
        break
    elif guess > number_to_guess:
        print("Too High")
    elif guess < number_to_guess:
        print("Too Low")

if n == difficulties[sel_difficult]-1:
    print(f"You Lose, Correct Answer {number_to_guess}!")