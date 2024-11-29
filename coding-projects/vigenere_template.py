"""This module is a simple vigenere cipher"""

from string import ascii_uppercase

LETTERS = ascii_uppercase


def main() -> None:
    """Handles the main logic of the vigenere cipher."""
    mode = get_mode()
    key = get_key()
    message = get_message(mode)
    translated_message = translate_message(mode, key, message)
    print_message(mode, translated_message)


def get_mode() -> str:
    """Get the mode from the user."""
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
    """Get the key from the user."""
    pass


def get_message(mode: str) -> str:
    """Get the message from the user."""
    pass


def translate_message(mode: str, key: str, message: str) -> str:
    """Encrypt or decrypt the message using the key."""
    pass


def print_message(mode: str, translated_message: str) -> None:
    """Print the mode and translated message."""
    pass


if __name__ == "__main__":
    main()
