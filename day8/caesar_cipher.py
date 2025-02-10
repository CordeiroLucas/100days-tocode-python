def encode(word, number):
    encoded = ''
    for letter in word:
        encoded += chr(ord(letter) + number)
    return encoded

def decode(word, number):
    decoded = ''
    for letter in word:
        decoded += chr(ord(letter) - number)
    return decoded

while True:
    choice = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:\n").lower()

    if choice == 'encode':
        message = input("Type the message: ")
        number = int(input("Type the number: "))

        encoded = encode(message, number)

        print(f"Here's the encoded result: {encoded}")
    elif choice == 'decode':
        message = input("Type the message:\n")
        number = int(input("Type the number:\n"))

        decoded = decode(message, number)

        print(f"Here's the decoded result: {decoded}")

    tryAgain = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.\n").lower()

    if tryAgain == "no":
        break
