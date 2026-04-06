import random

def calculate_score(your_cards):
    if sum(your_cards) == 21 and len(your_cards) == 2:
        return 0
    if sum(your_cards) > 21:
        for card in your_cards:
            if card == 11:
                your_cards.remove(11)
                your_cards.append(1)
        return sum(your_cards)
    return sum(your_cards)
def computer_calculate_score(computer_cards):
    if sum(computer_cards) == 21:
        return 0
    return sum(computer_cards)
def compare_scores(user_sum, computer_sum):
    if user_sum == computer_sum:
        return "Draw match"
    elif computer_sum == 0:
        return "Lose, Opponent has Blackjack"
    elif user_sum == 0:
        return "Win with a black jack"
    elif user_sum > 21:
        return "You went over. You lose"
    elif computer_sum > 21:
        return "Opponent went over. You lose"
    elif user_sum > computer_sum:
        return "You win"
    else:
        return "You lose"

def blackjack_game():
    card_pass = 'y'
    user_response = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = []
    length_of_cards = 2
    computer_cards = []
    computer_first_card = random.randint(2, 11)
    while user_response == 'y':
        while len(your_cards) < length_of_cards and card_pass == 'y':
            card1 = random.choice(cards)
            your_cards.append(card1)
            if(len(your_cards) >= 2):
                print(f"Your cards: {your_cards}, current score: {calculate_score(your_cards)}")
                print(f"Computer's first card: {computer_first_card}")
                if calculate_score(your_cards) == 0 or calculate_score(your_cards) > 21:
                    done = True
                else:
                    length_of_cards += 1
                    card_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if card_pass == 'n':
                        exit

        computer_cards.append(computer_first_card)
        while computer_calculate_score(computer_cards) < 17 and computer_calculate_score(computer_cards) != 0:
            computer_cards.append(computer_first_card)
            # while computer_calculate_score(computer_cards) < 17 and computer_calculate_score(computer_cards) != 0:
            computer_first_card = random.randint(2, 11)
            computer_cards.append(computer_first_card)
        print(f"Computer's final hand: {computer_cards}, final score: {computer_calculate_score(computer_cards)}")
        print(f"Your final hand: {your_cards}, final score: {calculate_score(your_cards)}")
        print(compare_scores(calculate_score(your_cards), computer_calculate_score(computer_cards)))
        print("\n" * 20)
        blackjack_game()



blackjack_game()



