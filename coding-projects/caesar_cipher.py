SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    mode = get_mode()
    key = get_key()

    # Let the user enter the message to encrypt/decrypt:
    print(f"Enter the message to {mode}.")
    message = input("> ")
    # Caesar cipher only works on uppercase letters:
    message = message.upper()
    translated = translate(mode, key, message)

    # Display the encrypted/decrypted string to the screen:
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
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ").upper()
        if not response.isdecimal():
            continue
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break
    return key


def translate(mode, key, message):
    # Stores the encrypted/decrypted form of the message:
    translated = ""
    # Encrypt/decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            # Get the encrypted (or decrypted) number for this symbol.
            num = SYMBOLS.find(symbol)  # Get the number of the symbol.
            if mode == "encrypt":
                num = (num + key) % len(SYMBOLS)
            elif mode == "decrypt":
                num = (num - key) % len(SYMBOLS)
            # Add encrypted/decrypted number's symbol to translated:
            translated += SYMBOLS[num]
        else:
            # Just add the symbol without encrypting/decrypting:
            translated += symbol
    return translated


if __name__ == "__main__":
    main()
