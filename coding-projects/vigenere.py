# Every possible symbol that can be encrypted/decrypted:
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    mode = get_mode()
    key = get_key()

    # Let the user specify the message to encrypt/decrypt:
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    translated = translate_message(message, key, mode)
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
    # Let the user specify the key to use:
    while True:  # Keep asking until the user enters a valid key.
        print("Please specify the key to use.")
        print("It can be a word or any combination of letters:")
        response = input("> ").upper()
        if response.isalpha():
            key = response
            break
    return key


def translate_message(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = []  # Stores the encrypted/decrypted message string.
    keyIndex = 0
    key = key.upper()
    for symbol in message:  # Loop through each character in message.
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not in LETTERS.
            if mode == "encrypt":
                # Add if encrypting:
                num += LETTERS.find(key[keyIndex])
            elif mode == "decrypt":
                # Subtract if decrypting:
                num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)  # Handle the potential wrap-around.
            # Add the encrypted/decrypted symbol to translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1  # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Just add the symbol without encrypting/decrypting:
            translated.append(symbol)
    return "".join(translated)


# If this program was run (instead of imported), run the program:
if __name__ == "__main__":
    main()
