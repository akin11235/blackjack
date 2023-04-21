'''
Blackjack - Game
'''

import sys
from random import randint
import time

def main():
    """my main function"""

    #deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('\nWelcome to Blackjack.')
    # print(f"{'':-<70}")

    def draw_new_card ():
        """Returns a randon number between 1 and 10"""
        return randint(1,10)

    def play_blackjack():
        """Blackjack game flow"""

        #The game begins by calling the function 'draw_new_card'
        #This assigns 2 random numbers to 2 variables for the player's starting cards
        #A third variable keeps track of the players' total starting cards
        player_card_1 = draw_new_card()
        player_card_2 = draw_new_card()
        player_total_at_start = player_card_1 + player_card_2

        print(f'\nYou draw a {player_card_1} and a {player_card_2}. '\
        f'Your total is {player_total_at_start}.\n')


        #The function 'draw_new_card' is called again
        #This assigns 2 random numbers to 2 variables for the dealer's starting cards
        #A third variable keeps track of the dealers' total starting cards
        dealer_card_1 = draw_new_card()
        dealer_card_2_hidden = draw_new_card()
        dealer_total_at_start = dealer_card_1 + dealer_card_2_hidden

        time.sleep(0.75)
        print(f'The dealer draws a {dealer_card_1} and a hidden card.\n')
        time.sleep(0.5)

        # ***********************PlAYER'S GAME PLAY BELOW***********************************

        #Assigning 2 variables for while loop for player's game
        player_last_total = player_total_at_start
        player_current_total = player_last_total

        #While loop checks players input for 'hit or stand' and handles invalid user input
        while player_current_total < 21:
            hit_or_stand = input('Hit or stand? (h/s): ').upper()
            if len(hit_or_stand) == 0 or hit_or_stand not in ['H','S']:
                print('\nYou have entered an incorrect entry\n')
                continue

            #Checks if player hits, assigns new random numbers and keeps track of the total
            if hit_or_stand == 'H':
                new_card = draw_new_card()
                player_current_total = player_last_total + new_card
                print(f'\nHit! You draw a {new_card}. Your total is '
                f'{player_current_total}. ', end='')
                player_last_total = player_current_total
                continue

            # Checks if the player stands
            print('\nYou stand.')
            time.sleep(0.5)
            print(f'\nThe dealer\'s hidden card is {dealer_card_2_hidden} and the dealer\'s '\
            f'total is {dealer_total_at_start}\n')
            break

        #Tests the total of the player and exits the game if the total > 21
        if player_current_total > 21:
            time.sleep(0.5)
            print('\n\nPLAYER BUSTED! DEALER WINS!!!!! GAME OVER\n')
            return

        #Tests the total of the player and continues the game if the total = 21
        if player_current_total == 21:
            time.sleep(0.5)
            print(f'Hit! You draw {new_card}. Your total is {player_current_total}.')
            time.sleep(0.5)
            print(f'\nThe dealer\'s hidden card is {dealer_card_2_hidden} and the dealer\'s '\
            f'total is {dealer_total_at_start}\n')


        #************************DEALER'S GAME PLAY******************************

        #Assigning 2 variables for while loop for dealer's game
        dealer_last_total = dealer_total_at_start
        dealer_current_total = dealer_last_total

        #While loop checks dealers start total and
        #calls the function 'draw_new_card' if dealer total is <= 16
        #While loop also calculates dealers total card value
        while dealer_current_total <= 16:
            time.sleep(1)
            print('The dealer hits.\n')
            new_card = draw_new_card()

            dealer_current_total = dealer_last_total + new_card
            time.sleep(1.5)
            print(f'The dealer is dealt a {new_card}. The dealer\'s total is '\
            f'{dealer_current_total}\n')
            dealer_last_total = dealer_current_total
            continue

        #Checks if the dealers total is between 17 and 21
        if 16 < dealer_current_total < 21:
            time.sleep(1)
            print('The dealer stands.\n')

        #Checks dealers total and exits game if it is > 21
        if dealer_current_total > 21:
            time.sleep(1)
            print('DEALER BUSTED!!!!\n')
            return

        #*******************DEALER VS PLAYER GAME RESULTS*************************

        # checks if dealer total = player total and exits the game
        if dealer_current_total == player_current_total:
            time.sleep(1)
            print(f'You have a total of {player_current_total} and the dealer has '
            f'{dealer_current_total}\n')
            time.sleep(1)
            print('\nDEALER WINS\n')
            return

        # checks if the dealer total > player total but less than 21. Exits game
        if player_current_total < dealer_current_total < 21:
            time.sleep(1)
            print(f'You have a total of {player_current_total} and the dealer has '
            f'{dealer_current_total}\n')
            time.sleep(1)
            print('DEALER WINS')
            return

    #While loop to continuously run the game
    while True:
        try: #validate user input at game start
            print(f"{'':-<70}")
            # time.sleep(0.5)
            new_game = input('\nDo you wish to start a new game? (y/n): ').upper()
            if len(new_game) == 0 or new_game not in ['Y','N']:
                time.sleep(1)
                print('\nYou have entered an incorrect entry\n')
                time.sleep(1)
                continue

            if new_game == 'Y':
                time.sleep(0.5)
                play_blackjack()
                continue

            time.sleep(0.5)
            print('\nBye!')
            sys.exit()

        except KeyboardInterrupt: #Exits game with a message if users types Control C
            print('\n\nYou have successfully quit the program. Please start again.')
            sys.exit()

if __name__ == '__main__':
    main()
