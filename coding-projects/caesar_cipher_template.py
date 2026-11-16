"""Caesar Cipher by <YOUR NAME HERE>."""

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    """Run the Caesar cipher program."""
    pass


def get_mode() -> str:
    """Ask the user for the mode and return "encrypt" or "decrypt"."""
    pass


def get_key() -> int:
    """Ask the user for the key and return it as an integer."""
    pass


def get_message(mode: str) -> str:
    """Ask the user for the message and return it in uppercase."""
    pass


def translate_message(mode: str, key: int, message: str) -> str:
    """Return the message encrypted or decrypted with the key."""
    pass


def print_message(mode: str, translated_message: str) -> None:
    """Print the mode and the translated message."""
    pass


if __name__ == "__main__":
    main()
