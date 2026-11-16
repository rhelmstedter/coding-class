"""Encrypt and decrypt messages with the Vigenère cipher."""

from itertools import cycle
from string import ascii_uppercase

LETTERS = ascii_uppercase


def main() -> None:
    """Run the Vigenère cipher program."""
    mode = get_mode()
    key = get_key()
    message = get_message(mode)
    translated_message = translate_message(mode, key, message)
    print_message(mode, translated_message)


def get_mode() -> str:
    """Ask the user for the mode and return "encrypt" or "decrypt"."""
    while True:
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()
        if response.startswith("e"):
            mode = "encrypt"
            break
        elif response.startswith("d"):
            mode = "decrypt"
            break
        print("Please enter the letter e or d.")
    return mode


def get_key() -> str:
    """Ask the user for the key and return it in uppercase."""
    while True:
        print("Please specify the key to use.")
        print("It can be a word or any combination of letters:")
        response = input("> ").upper()
        if response.isalpha():
            key = response
            break
        print("The key can only contain letters.")
    return key


def get_message(mode: str) -> str:
    """Ask the user for the message and return it in uppercase."""
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    return message


def translate_message(mode: str, key: str, message: str) -> str:
    """Return the message encrypted or decrypted with the key."""
    translated = []
    key_letters = cycle(key)
    for symbol in message:
        if symbol in LETTERS:
            idx = LETTERS.find(symbol)
            # Only move to the next key letter when a letter is translated.
            shift = LETTERS.find(next(key_letters))
            if mode == "encrypt":
                new_idx = (idx + shift) % len(LETTERS)
            elif mode == "decrypt":
                new_idx = (idx - shift) % len(LETTERS)
            translated.append(LETTERS[new_idx])
        else:
            # Spaces, numbers, and punctuation are not changed.
            translated.append(symbol)
    return "".join(translated)


def print_message(mode: str, translated_message: str) -> None:
    """Print the mode and the translated message."""
    print(f"{mode.title()}ed message:")
    print(translated_message)


if __name__ == "__main__":
    main()
