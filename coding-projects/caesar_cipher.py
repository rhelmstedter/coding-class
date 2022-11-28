LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    """Main function that handles logic of the program."""
    mode = get_mode()
    key = get_key()
    message = get_message(mode)
    translated_message = translate_message(mode, key, message)
    print_message(mode, translated_message)


def get_mode():
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


def get_key():
    """Get the key number from the user."""
    while True:
        max_key = len(LETTERS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ").upper()
        if not response.isdecimal():
            continue
        if 0 <= int(response) < len(LETTERS):
            key = int(response)
            break
    return key


def get_message(mode):
    """Get the message from the user."""
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    return message


def translate_message(mode, key, message):
    """Translate the message based on the mode (encrypt/decrypt) and key."""
    translated = ""
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == "encrypt":
                num = (num + key) % len(LETTERS)
            elif mode == "decrypt":
                num = (num - key) % len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol
    return translated


def print_message(mode, translated_message):
    """Print the mode and translated message."""
    print(f"{mode.title()}ed message:")
    print(translated_message)


if __name__ == "__main__":
    main()
