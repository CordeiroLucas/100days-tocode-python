word_list = ["bananal", "mongoloide", "banido", "twitch", "morango", "abacate"]

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chose_word. Then Print it.
import random

gameOver = False
while not gameOver:
    chose_word = random.choice(word_list).lower()

    correct_letters = []
    blanks_left = len(chose_word)
    for i in chose_word:
        correct_letters.append("_")

    lives = 5
    while not gameOver and blanks_left != 0:
        for i in correct_letters:
            print(f"{i}", end=" ")
        # print(f"\n|{blanks_left} blanks left|")

        guess = input("\n\nGuess a letter: ").lower()

        i = 0
        letter_in = False
        for letter in chose_word:
            if guess == letter:
                letter_in = True
            if guess == letter and guess != correct_letters[i]:
                correct_letters[i] = letter
                blanks_left -= 1
            i+=1

        if blanks_left == 0 and letter_in:
        
            print(f"\n**************** | You Win! The Word was \"{chose_word}\" | ****************\n")
            continue
            

        if not letter_in:
            if lives > 0:
                lives -= 1
                print(f"\n**************** | {lives} Vidas Faltando | ****************\n")
            else:
                gameOver = True
                print("\n**************** | Game Over! | ****************\n")

        
        if gameOver:
            entry = input("Play Again?: Y or N").lower()
            if entry == 'y':
                gameOver = False

