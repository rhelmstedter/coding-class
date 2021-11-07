# Let the user specify the message to hack:
print("Enter the encrypted Caesar cipher message to hack.")
message = input("> ")
# Every possible symbol that can be encrypted/decrypted:
# (This must match the LETTERS used when encrypting the message.)
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(len(LETTERS)):  # Loop through every possible key.
    translated = ""
    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)  # Get the number of the symbol.
            num = num - key  # Decrypt the number.
            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(LETTERS)
            # Add decrypted number's symbol to translated:
            translated = translated + LETTERS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol
    # Display the key being tested, along with its decrypted text:
    print(f"Key #{key}: {translated}")
