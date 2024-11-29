NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    """Stores the logic for the game loop."""
    # Print the Instructions outside the main game loop.
    print(
        f"""Instructions:\n
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:\n
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico."""
    )
    pass


def generate_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    pass


def get_guess():
    """Returns a valid guess from the user"""
    pass


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    pass


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
