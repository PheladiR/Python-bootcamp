import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😖"
    elif c_score == 0:
        return "Lose! Opponent has Blackjack 🙀"
    elif u_score == 0:
        return "You have a Blackjack! You win! 😼"
    elif u_score > 21:
        return "You lose. You went over. 😿"
    elif c_score > 21:
        return "Opponent went over. You win! 😼"
    elif u_score > c_score:
        return "You win! 😼"
    else:
        return "You lose! 😭"

def print_logo():
    logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/  

            🂡 Welcome to BLACKJACK 🃏
"""
    print(logo)

def play_game():
    print_logo()

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_card_deal = input("Type 'Y' to add another card, or 'N' to pass: ").upper()
            if user_card_deal == "Y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True


    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\nDo you want to play Blackjack? Type 'Y' or 'N': ").upper() == "Y":
    print("\n" + "*" * 20)
    play_game()
