# Imports
from art import logo
from modules import *

# --- Functions ---
def start():
    # Presentation
    print(logo)
    print(
        "Welcome to Blackjack by panxogol\n"
        "This project can be found at github.com/panxogol/python-blackjack\n"
        'This project was made in the context of the course "100 days of python" by Angela Yu at Udemy\n'
        "Enjoy the game!\n"
    )
    # Dictionary that contains the name of the card as key and the value or score of each one as value
    cards_values = create_cards()
    player_hand = deal_cards(cards_values)
    dealer_hand = deal_cards(cards_values)
    player_score = compute_score(player_hand, cards_values)

    print(f"Your hand is [{player_hand[0]}, {player_hand[1]}]. And your score is {player_score}.")
    print(f"The dealer has [{dealer_hand[0]}, X].")

    add_card = want_another_card()
    while add_card:
        give_card(player_hand, cards_values)
        player_score = compute_score(player_hand, cards_values)
        if player_score > 21:
            print(f"Your hand is now {player_hand} and your score is {player_score}.")
            print("Your score is greater than 21, so you lose. Sorry.")
            add_card = False
            if want_restart():
                start()
            return
        else:
            print(f"Your hand is now {player_hand} and your score is {player_score}.")
            add_card = want_another_card()

    dealer_has_won = not player_won(player_hand, dealer_hand, cards_values)
    dealer_score = compute_score(dealer_hand, cards_values)
    print(f"The dealer has {dealer_hand}, with a score of {dealer_score}.")
    while not dealer_has_won:
        if dealer_score < 17 or (dealer_score < player_score and dealer_score < 21):
            print("The dealer takes another card.")
            give_card(dealer_hand, cards_values)
            dealer_score = compute_score(dealer_hand, cards_values)
            print(f"The dealer has {dealer_hand}, with a score of {dealer_score}.")
            dealer_has_won = dealer_won(player_hand, dealer_hand, cards_values)
        else:
            break

    if player_score == dealer_score:
        print(f"It's a draw. You both have a score of {player_score}.")
    elif dealer_score > 21:
        print(f"Congratulations! You've won with a score of {player_score} vs the dealer's score: {dealer_score}.")
    elif player_won(player_hand, dealer_hand, cards_values):
        print(f"Congratulations! You've won with a score of {player_score} vs the dealer's score: {dealer_score}.")
    else:
        print(f"I'm sorry. You've lose with a score of {player_score} vs the dealer's score: {dealer_score}.")

    if want_restart():
        start()
    else:
        return

# start and play
start()
