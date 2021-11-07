# Every possible symbol that can be encrypted/decrypted:
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    mode = get_mode()
    key = get_key()

    # Let the user specify the message to encrypt/decrypt:
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    translated = translate_message(message, key, mode)

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
    ...


def translate_message():
    ...


# If this program was run (instead of imported), run the program:
if __name__ == "__main__":
    main()
