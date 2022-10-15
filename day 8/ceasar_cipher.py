#encoding text like Caesar
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direct, text_input, shift_amount):
    new_text = ""
    shift_amount = shift_amount % 26
    if direct == "decode":
        shift_amount *= -1
    for letter in text_input:
        if letter in alphabet:
            new_text += alphabet[alphabet.index(letter)+shift_amount]
        else:
            new_text += letter
    print(f"The {direct}d text is {new_text}")
    go_on = input("Do you want to restart? Type 'yes' if you want to go again and 'no' to end the program:\n")
    if go_on == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(direction, text, shift)
