# ------------------------------------------------------------
# Task 1: Hangman Game (CodeAlpha Python Internship)
# The computer picks a secret word and the player guesses it
# one letter at a time. 6 wrong guesses and the player loses.
# ------------------------------------------------------------

import random

# 5 predefined words, each with a small hint
words = {
    "python": "A popular programming language",
    "laptop": "You are probably using one right now",
    "keyboard": "You type on it",
    "internet": "It connects computers around the world",
    "database": "A place where data is stored",
}

MAX_WRONG = 6

# The hangman drawing for 0 to 6 wrong guesses
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def get_display_word(word, guessed_letters):
    """Return the word with _ for letters that are not guessed yet."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    return display


def play_game():
    """Play one round. Returns True if the player wins, else False."""
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    wrong_guesses = 0

    print("\nA new word has been chosen!")
    print("It has", len(word), "letters.")
    print("Hint:", hint)

    while wrong_guesses < MAX_WRONG:
        print(stages[wrong_guesses])
        print("Word:", get_display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(guessed_letters))
        print("Wrong guesses left:", MAX_WRONG - wrong_guesses)

        guess = input("Guess a letter: ").lower().strip()

        # check that the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed", guess, "- try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!", guess, "is in the word.")
        else:
            wrong_guesses = wrong_guesses + 1
            print("Sorry,", guess, "is not in the word.")

        # check if all letters are guessed
        if "_" not in get_display_word(word, guessed_letters):
            print("\nWord:", get_display_word(word, guessed_letters))
            print("Congratulations, you won! The word was:", word)
            return True

    # the loop ended, so the player used all the guesses
    print(stages[MAX_WRONG])
    print("Game over! The word was:", word)
    return False


def main():
    print("=" * 40)
    print("        WELCOME TO HANGMAN")
    print("=" * 40)
    print("Guess the word one letter at a time.")
    print("You are allowed", MAX_WRONG, "wrong guesses.")

    wins = 0
    losses = 0

    while True:
        if play_game():
            wins = wins + 1
        else:
            losses = losses + 1

        print("\nScore -> Wins:", wins, "| Losses:", losses)

        # ask if the player wants to play again
        while True:
            again = input("Play again? (y/n): ").lower().strip()
            if again == "y" or again == "n":
                break
            print("Please type y or n.")

        if again == "n":
            print("Thanks for playing. Goodbye!")
            break


main()
