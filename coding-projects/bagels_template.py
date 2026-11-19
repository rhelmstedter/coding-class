"""Bagels by <YOUR NAME HERE>."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10
INSTRUCTIONS = f"""Instructions:

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. I will give you clues about your guess:

When I say:    That means:
  Pico           One digit is correct but in the wrong position.
  Fermi          One digit is correct and in the right position.
  Bagels         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
"""


def generate_secret_num() -> str:
    """Return a string made up of NUM_DIGITS unique random digits."""
    pass


def get_guess() -> str:
    """Keep asking until the user enters a valid guess, then return it."""
    pass


def get_clues(guess: str, secret_num: str) -> str:
    """Return a string with the Pico, Fermi, Bagels clues for a guess."""
    pass


def main() -> None:
    """Run the game loop."""
    pass


if __name__ == "__main__":
    main()
