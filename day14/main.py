from game_data import data
import random
import os
from library import *

play_again = 'y'
high_score = 0

while play_again == 'y':

    os.system('cls')

    card_data = data.copy()

    score = 0
    game_over = False

    print(data_is_empty(card_data))
    
    actual_card = random.choice(card_data)
    card_data.remove(actual_card)

    while not game_over and not data_is_empty(card_data):
        os.system('cls')
        
        compared_card = random.choice(card_data)
        card_data.remove(compared_card)

        print_scores(score, high_score)
        print_cards(actual_card, compared_card)

        print_options(actual_card, compared_card)
        option = int(input("-> "))

        higher_card = compare(compared_card, actual_card)

        if (higher_card == compared_card and option == 1) or (higher_card == actual_card and option == 2):
            actual_card = compared_card
            score += 1

        else:            
            game_over = True

            print_total_followers(actual_card, compared_card)
            print_scores(score, high_score)

            print(GAME_OVER_MESSAGE)           

            print(PLAY_AGAIN_MESSAGE)
            play_again = input("-> ").lower()

        high_score = update_highscore(score, high_score)

        if data_is_empty(card_data):
            game_over = True
            
            print_scores(score, high_score)

            print(PLAY_AGAIN_MESSAGE)
            play_again = input("-> ").lower()