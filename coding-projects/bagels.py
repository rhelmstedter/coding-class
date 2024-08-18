"""A Python Version of Bagels."""
import random


NUM_DIGITS = 3
MAX_GUESSES = 3
INSTRUCTIONS = f"""Instructions:\n
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. I will give you clues about your guess:
When I say:    That means:
  Pico           One digit is correct but in the wrong position.
  Fermi          One digit is correct and in the right position.
  Bagels         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.\n"""

def generate_secret_num() -> str:
    """Return a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    return "".join(numbers[:3])

def get_guess() -> str:
    """Get the clue from the user."""
    while True:
        guess = input("> ")
        if len(guess) != NUM_DIGITS or not guess.isdecimal():
            print("Enter a valid guess.")
            continue
        else:
            break
    return guess

def get_clues(guess, secret_num) -> str:
    """Calculate the clues."""
    if guess == secret_num:
        return "You got it!"
    clues = []
    for guess_digit, secret_digit in zip(guess, secret_num):
        if guess_digit == secret_digit:
            # A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess_digit in secret_num:
            # A correct digit is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all.
    else:
        clues.sort()
        return " ".join(clues)

def main():
    """Store the logic of the game loop."""
    # Print the instructions outside the game loop.
    print(INSTRUCTIONS)
    while True:  # Main game loop.
        # Create secret number
        secret_num = generate_secret_num()
        print(f"I have thought of a number that is {NUM_DIGITS} digits long.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        # Create game logic loop.
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = get_guess()
            # Create loop for user input and make sure it is valid.
            print(f"Guess #{num_guesses}: ")

            # Get the clues based on the user input
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They"re correct, so break out of this loop.
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        # Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")

# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
