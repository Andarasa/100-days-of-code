direction = input("Type encode to encrypt, type decode to decrypt\n").lower()
text = input("What message do you want to encode?\n").lower()
letter_shift = int(input("How many letters do you want to shift by?\n"))

alphabet = ["a" , "b" , "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encrypt(original_text, shift_amount):
    cypher_text = ""

    for letter in original_text:
        shifted_position= alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cypher_text += alphabet[shifted_position]

    print(f"Here is your encoded result: {cypher_text}")

def decrypt(original_text, shift_amount):
    cypher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position  %= len(alphabet)
        cypher_text += alphabet[shifted_position]

    print(f"Here is your decoded result: {cypher_text}")

if direction == "encode":
    encrypt(text, letter_shift)
elif direction == "decode":
    decrypt(text, letter_shift)

