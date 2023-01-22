'''
Blackjack - Game requirements
1.  The possible card values range from 1 to 10 and,
unlike a real deck, the probability of drawing a card is equal

2. The game begins by dealing two visible cards to the player, and two cards to the dealer.
However, in the case of the dealer, one card is visible to other player while the other is hidden.

3.  The player decides whether to "hit" (draw another card), or "stand" which ends their turn.

4.  The player may hit any number of times. Should the total of the cards exceed 21,
the player "busts" and loses the game to the dealer. The round then ends and
the dealer does not have to draw/show any additional cards.

5.  If the player reaches 21, the player stands

6.  The dealer's turn begins by revealing the hidden card

7.  The dealer must continue to hit if the total is 16 or less,
and must stand if the value is 17 or more

8.  The dealer busts if their total is over 21 and the player wins.

9.  The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)

10. The program indicates who the winner is and asks to play again

11. It is up to you as the developer on how you will choose to handle invalid
user input, but note the program cannot crash upon invalid input.
Options can involve asking the user again or exiting the program with a user-friendly message.
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
