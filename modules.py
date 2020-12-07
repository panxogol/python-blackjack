from random import choice

# Creates the cards
def create_cards():
    """
    Creates a dictionary with the values of the cards in blackjack.
    """
    return {
        "A": (0, 11),
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }

# deal cards
def deal_cards(cards: dict):
    """
    Deal two cards to a player as a list
    """
    hand = [choice(list(cards)), choice(list(cards))]
    return hand

# Compute the score of a hand
def compute_score(hand: list, cards: dict):
    """
    It returns the score of a blackjack hand
    """
    score = 0
    for card in hand:
        if card == "A":
            if score + cards[card][1] > 21:
                score += cards[card][0]
            else:
                score += cards[card][1]
        else:
            score += cards[card]

    return score

# ask the player for another card
def want_another_card():
    """
    Ask the user if wants a new card. Case yes: return True, case no: return False.
    """
    print("Do you want to add one more card?")
    answer = input("Please write (y)es or (N)o: ").lower()
    while answer != "y" and answer != "n":
        print("You've entered a wrong answer. Try again.")
        answer = input("Please write (y)es or (N)o: ").lower()
    if answer == "y":
        return True
    else:
        return False

# Compare two hands
def player_won(player_hand: list, dealer_hand: list, cards: dict):
    """
    compare the two hands inside and returns true if the first one won, returns false in the other case.
    """
    player_score = compute_score(player_hand, cards)
    dealer_score = compute_score(dealer_hand, cards)

    if player_score > 21:
        return False
    elif player_score > dealer_score:
        return True
    else:
        return False

# Dealer won
def dealer_won(player_hand: list, dealer_hand:list, cards:dict):
    """
    Check if dealer has a better hand than the player, returns True in that case, False in the other case.
    """
    player_score = compute_score(player_hand, cards)
    dealer_score = compute_score(dealer_hand, cards)

    if dealer_score > 21:
        return False
    elif dealer_score > player_score:
        return True
    else:
        return False

# Give a card to the player
def give_card(hand: list, cards: dict):
    """
    Add a new card to the selected hand
    """
    new_card = choice(list(cards))
    print(f"The new card is {new_card}.")
    hand.append(new_card)

# Checks if player wants to play again
def want_restart():
    print("Do you want to play again?")
    answer = input("Please answer (y)es or (n)o: ").lower()
    while answer != "y" and answer != "n":
        print("Wrong answer, please try again.")
        answer = input("Please answer (y)es or (n)o: ").lower()
    if answer == "y":
        return True
    else:
        return False
