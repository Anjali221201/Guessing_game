# Guessing_game
'Find the Ball' Guessing Game!

A simple Python console game where the player tries to guess the location of a hidden object ("O") in a shuffled list. This game uses randomization to mix up the list and challenges the player to pick the correct index.

## How to Play

1. The game starts by shuffling a list that contains one hidden object ("O") and two empty slots (" ").
2. The player is prompted to guess the position of "O" by entering an index (0, 1, or 2).
3. If the player correctly guesses the position of "O", they win the round. Otherwise, they are informed of an incorrect guess and shown the list to see where "O" was hidden.

## Game Structure

- **shuffle_list**: Shuffles the list to randomize the position of "O".
- **player_guess**: Takes input from the player and ensures the input is a valid index (0, 1, or 2).
- **check_guess**: Checks if the player’s guess is correct and provides feedback.



## How to Run the Game

1. Make sure you have Python installed.
2. Clone this repository or copy the code into a Python file (e.g., `Guessing_game.py`).
3. Run the script from your terminal:
   ```bash
   Guessing_game.py
   ```

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you have suggestions for improvements, please create a pull request or open an issue.
