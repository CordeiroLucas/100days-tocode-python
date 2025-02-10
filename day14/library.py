global GAME_OVER_MESSAGE 
global PLAY_AGAIN_MESSAGE

GAME_OVER_MESSAGE = "\n================== GAME OVER! =====================\n" 
PLAY_AGAIN_MESSAGE = "Play Again? 'y' or 'n'" 

def print_scores(score, high_score):
    """Only a print function"""
    print(f'\n======= SCORE {score} ========== HIGH SCORE {high_score} ==========\n')

def print_cards(card1, card2):
    """Only a print function"""
    for info in card1:        
        print(card1[info])

    print("\nVS\n")

    for info in card2:
        if info != 'follower_count':
            print(card2[info])
    print("------------------------------\n")

def print_options(card1, card2):
    """Display the compare options to user"""
    print(f"Does {card2['name']} has:\n")
    print("'1' to Higher\n'2' to Lower\n")
    print(f"Followers Than {card1['name']}?\n")

def print_total_followers(card1, card2):
    """Display the followers of both cards"""
    print(f"{card1['name']} has {card1['follower_count']},000,000 followers!")
    print("VS")
    print(f"{card2['name']} has {card2['follower_count']},000,000 followers!\n")

def update_highscore(score, high_score):
    """Return the higher score"""
    if score > high_score:
        return score
    else: return high_score

def compare(card1, card2):
    """Return the card with higher followers"""
    if card1['follower_count'] >= card2['follower_count']:
        return card1
    else: return card2

def data_is_empty(cards):
    """Check if the database still have data available"""
    if len(cards) == 0:
        return True
    else: return False