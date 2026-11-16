"""Encrypt and decrypt messages with the Caesar cipher."""

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    """Run the Caesar cipher program."""
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


def get_key() -> int:
    """Ask the user for the key and return it as an integer."""
    max_key = len(LETTERS) - 1
    while True:
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ")
        if response.isdecimal() and int(response) <= max_key:
            key = int(response)
            break
        print(f"The key must be a whole number from 0 to {max_key}.")
    return key


def get_message(mode: str) -> str:
    """Ask the user for the message and return it in uppercase."""
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    return message


def translate_message(mode: str, key: int, message: str) -> str:
    """Return the message encrypted or decrypted with the key."""
    translated = ""
    for symbol in message:
        if symbol in LETTERS:
            idx = LETTERS.find(symbol)
            if mode == "encrypt":
                new_idx = (idx + key) % len(LETTERS)
            elif mode == "decrypt":
                new_idx = (idx - key) % len(LETTERS)
            translated += LETTERS[new_idx]
        else:
            # Spaces, numbers, and punctuation are not changed.
            translated += symbol
    return translated


def print_message(mode: str, translated_message: str) -> None:
    """Print the mode and the translated message."""
    print(f"{mode.title()}ed message:")
    print(translated_message)


if __name__ == "__main__":
    main()
