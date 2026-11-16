"""Hack the Caesar cipher by trying every possible key (brute force)."""

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    """Run the Caesar hacker program."""
    message = get_message()
    hack_message(message)


def get_message() -> str:
    """Ask the user for the encrypted message and return it in uppercase."""
    print("Enter the encrypted Caesar cipher message to hack.")
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


def hack_message(message: str) -> None:
    """Print the message decrypted with every possible key."""
    for key in range(len(LETTERS)):
        translated_message = translate_message("decrypt", key, message)
        print(f"Key #{key}: {translated_message}")


if __name__ == "__main__":
    main()
