import random

# Create a list of words
hangman_words = [
    "apple", "banana", "cat", "dog", "elephant",
    "fish", "grape", "house", "ice", "jelly",
    "kite", "lion", "monkey", "nest", "orange",
    "pencil", "queen", "rabbit", "sun", "tree"
]

# Pick a word from the list
random_word = random.choice(hangman_words)

# Initialize display word with underscores
display_word = "_" * len(random_word)

# Set the number of attempts
attempts = len(random_word)  

# Main game loop
while attempts > 0 and "_" in display_word:
    # Print the current state of the word
    print(" ".join(display_word))
    print(f"Attempts remaining: {attempts}")

    # Grab input from user
    guess_char = input("Please guess a character: ").lower()  # Convert to lowercase

    # Check if the guessed character is in the word
    if guess_char in random_word:
        # Update the display word with the guessed character
        display_word = "".join(
            [guess_char if random_word[i] == guess_char else display_word[i] for i in range(len(random_word))]
        )
        print(f"Good guess! '{guess_char}' is in the word.")
    else:
        # Decrement attempts if the guess is incorrect
        attempts -= 1
        print(f"Sorry, '{guess_char}' is not in the word. You have {attempts} attempts left.")

    # Print the updated word
    print(f"Updated word: {' '.join(display_word)}")
    print("-" * 40)  # Separator for clarity

# Game over message
if "_" not in display_word:
    print(f"Congratulations! You guessed the word: {random_word}")
else:
    print(f"Game over! The word was: {random_word}")


