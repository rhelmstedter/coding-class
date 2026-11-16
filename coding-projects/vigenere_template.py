"""Vigenère Cipher by <YOUR NAME HERE>."""

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
    pass


def get_message(mode: str) -> str:
    """Ask the user for the message and return it in uppercase."""
    pass


def translate_message(mode: str, key: str, message: str) -> str:
    """Return the message encrypted or decrypted with the key."""
    pass


def print_message(mode: str, translated_message: str) -> None:
    """Print the mode and the translated message."""
    pass


if __name__ == "__main__":
    main()
