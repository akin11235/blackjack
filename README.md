# Blackjack Game in Python

## Project Overview
This Python application implements a simplified version of the Blackjack card game. The game features a straightforward interface for a single player to play against a dealer, with the ability to "hit" or "stand" based on standard Blackjack rules.

### Game Rules
- **Card Values**: The possible card values range from 1 to 10, with equal probability for each card.
- **Dealing Cards**: The game begins by dealing two visible cards to the player and two cards to the dealer. One dealer card is visible to the player, while the other is hidden.
- **Player Actions**: The player can choose to "hit" (draw another card) or "stand" (end their turn). The player may hit as many times as desired, but if the total card value exceeds 21, the player "busts" and loses the game.
- **Dealer Actions**: The dealer reveals their hidden card and must continue to hit if the total card value is 16 or less. The dealer stands if the total is 17 or more. The dealer busts if their total exceeds 21, resulting in a win for the player.
- **Winning and Ties**: If both the dealer and player reach 21, the dealer wins. The program indicates the winner and offers the option to play again.

### Key Features
- **Interactive Game Play**: Allows the player to choose between hitting or standing, with appropriate prompts and instructions.
- **Dealer Logic**: Implements dealer behavior according to Blackjack rules, including handling of the dealer's hidden card.
- **Game Outcome**: Determines and displays the game result (win, lose, or tie) and prompts the user to play again.
- **Input Handling**: Manages invalid user input gracefully without crashing the program.

## How to Set Up and Run the Game
1. **Clone the Repository**  
   Clone the repository from GitHub to your local machine:
    ```bash
    git clone https://github.com/akin11235/blackjack.git
    ```

2. **Navigate to the Project Directory**  
   Change your working directory to the project directory:
    ```bash
    cd Blackjack
    ```

3. **Run the Game**  
   Execute the Python script to start the game:
    ```bash
    python blackjack.py
    ```

4. **Play the Game**  
   Follow the prompts to play the game. You will be asked to hit or stand, and the game will continue based on your choices.

5. **Restart or Exit**  
   After each round, the game will indicate the winner and prompt you to play again or exit.

6. **Change Git Remote URL**  
    To avoid accidental pushes to the base project, change the Git remote URL:
    ```bash
    git remote set-url origin https://github.com/yourusername/Blackjack.git
    git remote -v # confirm the changes
    ```

7. **Clean Up**  
   To clean up any unnecessary files or directories, you can remove temporary files or caches:
    ```bash
    rm -rf __pycache__
    ```

## Additional Information
- **Python Documentation**: [Python Documentation](https://docs.python.org/3/)
- **Blackjack Rules**: [Blackjack Rules](https://www.blackjack.org/rules/)

---
