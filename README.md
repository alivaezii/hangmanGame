# hangmanGame
This is a simple implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list, and the player has to guess the word by suggesting letters within a limited number of attempts.

## How to Play
Start the Game: Run the Python script to start the game.

Guess a Letter: You will be prompted to guess a letter. Enter a single character.

## Feedback:

If the guessed letter is in the word, the game will reveal all instances of that letter in the word.

If the guessed letter is not in the word, you will lose one attempt.

## Win or Lose:

You win if you guess all the letters in the word before running out of attempts.

You lose if you run out of attempts before guessing the word.

## Code Overview
Variables
hangman_words: A list of words from which the game randomly selects one.

random_word: The word randomly chosen from the list.

display_word: A string of underscores representing the letters of the word to be guessed.

attempts: The number of attempts the player has to guess the word.

## Game Loop
The game continues until the player either guesses the word or runs out of attempts.

The player is prompted to guess a letter, and the game checks if the letter is in the word.

The display_word is updated to reflect correctly guessed letters.

The number of attempts decreases with each incorrect guess.

## Game Over
If the player guesses the word correctly, a congratulatory message is displayed.

If the player runs out of attempts, the game reveals the correct word.

## Example Output
_ _ _ _ _
Attempts remaining: 5
Please guess a character: a
Good guess! 'a' is in the word.
Updated word: _ a _ _ _
----------------------------------------
_ a _ _ _
Attempts remaining: 5
Please guess a character: z
Sorry, 'z' is not in the word. You have 4 attempts left.
Updated word: _ a _ _ _
----------------------------------------
...

## Requirements
Python 3.x

## How to Run
Save the code in a file, e.g., hangman_game.py.

Open a terminal or command prompt.

Navigate to the directory where the file is saved.

Run the script using the command:

python hangman_game.py 

## Customization
Word List: You can modify the hangman_words list to include your own set of words.

Attempts: Adjust the number of attempts by changing the attempts variable.