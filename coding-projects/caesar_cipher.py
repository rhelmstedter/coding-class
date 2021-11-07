LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    mode = get_mode()
    key = get_key()

    # Let the user enter the message to encrypt/decrypt:
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    translated = translate_message(mode, key, message)

    # Display the encrypted/decrypted string to the screen:
    print(f"{mode.title()}ed message:")
    print(translated)


def get_mode():
    while True:  # Keep asking until the user enters e or d.
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
    # Let the user enter the key to use:
    while True:  # Keep asking until the user enters a valid key.
        max_key = len(LETTERS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ").upper()
        if not response.isdecimal():
            continue
        if 0 <= int(response) < len(LETTERS):
            key = int(response)
            break
    return key


def translate_message(mode, key, message):
    # Stores the encrypted/decrypted form of the message:
    translated = ""
    # Encrypt/decrypt each symbol in the message:
    for symbol in message:
        if symbol in LETTERS:
            # Get the encrypted (or decrypted) number for this symbol.
            num = LETTERS.find(symbol)  # Get the number of the symbol.
            if mode == "encrypt":
                num = (num + key) % len(LETTERS)
            elif mode == "decrypt":
                num = (num - key) % len(LETTERS)
            # Add encrypted/decrypted number's symbol to translated:
            translated += LETTERS[num]
        else:
            # Just add the symbol without encrypting/decrypting:
            translated += symbol
    return translated


if __name__ == "__main__":
    main()
