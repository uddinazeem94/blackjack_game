import random
import time

from replit import clear
from time import sleep

logo = """

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
      
"""

list_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def win(player,computer):
    if player == computer:
        print("You draw")
    elif player > computer:
        print("You Win!!")
    elif computer > 21:
        print("You Win!!")
    else:
        print("You Lose!!")


def random_card(player):
    card = random.choice(list_cards)
    player.append(card)


def check_for_a(player):
    for each in player:
        if each == 'A':
            player.remove('A')
            if sum(player) < 11:
                player.append(11)
            else:
                player.append(1)

clear()
print(logo)
def blackjack():
    time.sleep(1)
    # Creating empty list for computer and myself
    my_cards = []
    random_card(my_cards)
    com_cards = []
    random_card(com_cards)
    time.sleep(1)

    no_deal = False
    while no_deal is not True:
        random_card(my_cards)
        check_for_a(my_cards)
        print(f"Your Cards:{my_cards}, Computer cards:{com_cards}")

        my_score = sum(my_cards)
        print(f"Your Score is: {my_score}")
        if my_score == 21:
            no_deal= True

        elif my_score < 21:
            deal = input("Type 'y' to deal or 'n' to pass: ").lower()
            if deal == 'n':
                no_deal = True
        else:
            no_deal = True
    time.sleep(1.5)

    if my_score > 21:
        print("You went over 21.. You Lose!")
    else :
        random_card(com_cards)
        check_for_a(com_cards)
        print(f"Your Cards:{my_cards}, Computer cards:{com_cards}")
        time.sleep(1)
        com_score = sum(com_cards)
        if com_score < 16 and len(com_cards) < 4:
            print('Computer is taking a deal')
            time.sleep(1.5)
            random_card(com_cards)
            check_for_a(com_cards)
            com_score = sum(com_cards)
            len(com_cards)
        print(f"Your Cards:{my_cards}, Computer cards:{com_cards}")
        print(f"Your Score is: {my_score} Computer Score is: {com_score}")
        win(my_score,com_score)
    time.sleep(1.5)
    run = input("Do you want to play again?\nReply 'y' for YES or 'n' for NO ").lower()
    if run == 'y' or run == 'yes':
        blackjack()
    elif run == 'n' or 'no':
        exit()


print("Welcome to my Blackjack Program")
no_run = False
while no_run is not True:
    start = input("Would you like to play a game of blackjack with me?").lower()
    if start == 'y' or start == 'yes':
        blackjack()
    elif start == 'n' or start == 'no':
        exit()
    else:
        print("Invalid answer.Try Again")

