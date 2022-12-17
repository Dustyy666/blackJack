import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "in with BlackJack"
    elif user_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "Opponent went over 21. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            want_card = input("Want another card? Y/N ").lower()
            if want_card == "y":
                user_cards.append(deal_card())
                print(user_cards)
            else:
                game_over = True

    while computer_score != 0 and computer_score <= 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, Your total was: {user_score}")
    print(
        f" Computer's final hand: {computer_cards}, Opponent total was: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input(
        "Do you want to play a game of BlackJack? Type 'y' for Yes, and 'n' for No: "
) == "y":
    os.system('cls')
    play_game()