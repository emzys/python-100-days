from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def ceasarCipher(direction, text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            # if direction == "decode": shift *= -1
            position = position + shift if direction == "encode" else position - shift
            if direction == "encode" and position >= len(alphabet):
                position = position - len(alphabet)
            cipher_text += alphabet[position]
        else:
            cipher_text += letter

    print(f"The {direction}d text is {cipher_text}")


end_program = False
print(logo + "\n\n")
while not end_program:
    # print(logo + "\n\n")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = int(shift) % 26
    ceasarCipher(direction, text, shift)
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        end_program = True
        print("Goodbye")
