import random
import art
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = []
computer_card = []
def card_calculator(card_list):
    total = 0
    for card in card_list:
        total += card
    return total
def card_picker():
    card = [random.choice(cards), random.choice(cards)]
    return card

def computer(computer_cards):
    total = card_calculator(computer_cards)
    while total <=21:
        is_in_computer = False

        if total < 17:
            computer_cards.append(random.choice(cards))
            total = card_calculator(computer_cards)
            if total == 21:
                return computer_cards
            elif total > 21:
                num = 0
                for i in computer_cards:
                    if i == 11:
                        is_in_computer = True
                        computer_cards[num] = 1
                        break
                    num += 1
                total = card_calculator(computer_cards)
                if not is_in_computer:
                    return computer_cards


        elif total > 17:
            return computer_cards

    return computer_cards


def player():
    p_card = card_picker()
    c_card = card_picker()
    total = card_calculator(p_card)
    print(f"your card are: {p_card} and total is: {total}")
    print(f"computer card are: {c_card[0]}")

    while total <= 21:
        is_in_player = False
        if total == 21:
            return p_card, c_card
        choice = input("hit or stand?(y/n)")
        if choice == "y":
            p_card.append(random.choice(cards))
            total = card_calculator(p_card)
            if total == 21:
                c_card = computer(c_card)
                return p_card, c_card
            elif total > 21:
                num = 0
                for i in p_card:
                    if i == 11:
                        is_in_player = True
                        p_card[num] = 1
                        break
                    num += 1
                total = card_calculator(p_card)
                if not is_in_player:
                    return p_card, c_card
            print(f"your card are: {p_card} and total is: {total}")
            print(f"computer card are: {c_card[0]}")

        if choice == "n":
            c_card = computer(c_card)
            return p_card , c_card
    return p_card, c_card


def play_game():
    game = True
    while game:
        event = input("want to play (y/n)")
        if event == "y":
            p , c = player()
            p_total = card_calculator(p)
            c_total = card_calculator(c)
            if p_total == c_total:
                print(f"your cards are: {p} and total is: {p_total}")
                print(f"computer cards are: {c} and total is: {c_total}")
                print("draw")

            elif p_total > 21:
                print(f"your cards are: {p} and total is: {p_total}")
                print(f"computer cards are: {c} and total is: {c_total}")
                print("you loss")

            elif c_total > 21:
                print(f"your cards are: {p} and total is: {p_total}")
                print(f"computer cards are: {c} and total is: {c_total}")
                print("you win")
            elif p_total > c_total:
                print(f"your cards are: {p} and total is: {p_total}")
                print(f"computer cards are: {c} and total is: {c_total}")
                print("you win")
            else:
                print(f"your cards are: {p} and total is: {p_total}")
                print(f"computer cards are: {c} and total is: {c_total}")
                print("you lose")

        elif event == "n":
            game = False

play_game()
