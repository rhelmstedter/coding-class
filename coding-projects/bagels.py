"""A Python version of Bagels, a deductive logic game."""

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
    numbers = list("0123456789")
    random.shuffle(numbers)
    return "".join(numbers[:NUM_DIGITS])


def get_guess() -> str:
    """Keep asking until the user enters a valid guess, then return it."""
    while True:
        guess = input("> ")
        if len(guess) == NUM_DIGITS and guess.isdecimal():
            break
        print(f"Enter a valid guess: {NUM_DIGITS} digits, no letters.")
    return guess


def get_clues(guess: str, secret_num: str) -> str:
    """Return a string with the Pico, Fermi, Bagels clues for a guess."""
    clues = []
    for guess_digit, secret_digit in zip(guess, secret_num):
        if guess_digit == secret_digit:
            clues.append("Fermi")
        elif guess_digit in secret_num:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    clues.sort()
    return " ".join(clues)


def main() -> None:
    """Run the game loop."""
    print(INSTRUCTIONS)
    while True:
        secret_num = generate_secret_num()
        print(f"I have thought of a number that is {NUM_DIGITS} digits long.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            print(f"Guess #{num_guesses}: ")
            guess = get_guess()
            if guess == secret_num:
                print("You got it!")
                break
            print(get_clues(guess, secret_num))
            num_guesses += 1

        if num_guesses > MAX_GUESSES:
            print("You ran out of guesses.")
            print(f"The answer was {secret_num}.")

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
