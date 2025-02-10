import random
import os

# A -> 11 or 1| Q -> 10 | J -> 10 | K -> 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def lose_condition(deck):
    if sum(deck) > 21:
        return True
    else: return False

def win_condition(deck):
    if sum(deck) == 21:
        return True
    else: return False

def calculate_score(deck):
    card = random.choice(cards)
    deck.append(card)

    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    
    return sum(deck)

def print_result(deck1, deck2):
    print(f"\tYour final hand: {deck1}, final score {sum(deck1)}")
    print(f"\tComputer's final hand: {deck2}, final score {sum(deck2)}")

def is_game_over(deck1, deck2):
    if sum(deck1) == sum(deck2):
        return [True, 0]
    elif win_condition(deck1) or lose_condition(deck2):
        return [True, 1] # 1 é o Player
    elif win_condition(deck2) or lose_condition(deck1):
        return [True, -1] # -1 é o Computador
    else: return [False, 0]



while True:
    game_active = input(f"Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()

    player_deck = []
    computer_deck = []

    player_deck = [random.choice(cards), random.choice(cards)]
    computer_deck = [random.choice(cards), random.choice(cards)]

    if game_active == 'y':
        while (not is_game_over(player_deck, computer_deck)[0]) and game_active == 'y': #Game Active
            os.system('cls')
            while True:
                print(f"\t Your cards: {player_deck}, current score {sum(player_deck)}")
                print(f"\t Computer's first card: {computer_deck[0]}")

                get_card = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()

                if get_card == 'y':
                    if calculate_score(player_deck) >= 21:
                        break
                else:
                    break

            while True and get_card == 'n':
                cpu_option = random.randint(0,1)
                if cpu_option == 1:
                    if calculate_score(computer_deck) >= 21:
                        break
                
            game_over = is_game_over(player_deck, computer_deck)
            if game_over[0]:
                match game_over[1]:
                    case 1:
                        print_result(player_deck, computer_deck)
                        print("You Win ")
                    
                    case -1:
                        print_result(player_deck, computer_deck)
                        print("You Lose")
                        
                    case 0:
                        print_result(player_deck, computer_deck)
                        print("Draw")
                break

    if game_active == 'n': break
                    

