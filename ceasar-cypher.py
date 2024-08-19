direction = input("Type encode to encrypt, type decode to decrypt\n").lower()
text = input("What message do you want to encode?\n").lower()
letter_shift = int(input("How many letters do you want to shift by?\n"))

alphabet = ["a" , "b" , "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

   

def ceasar(original_text, shift_amount, encode_or_decode):
    cypher_text = ""

    for letter in original_text:
        if letter not in alphabet:
            cypher_text += letter
        else:
            if direction == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
            elif direction == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
            shifted_position  %= len(alphabet)
            cypher_text += alphabet[shifted_position]
    print(f"Here is your decoded result: {cypher_text}")


should_continue = True

while should_continue:

    direction = input("Type encode to encrypt, type decode to decrypt\n").lower()
    text = input("What message do you want to encode?\n").lower()
    letter_shift = int(input("How many letters do you want to shift by?\n"))

    ceasar(original_text=text, shift_amount=letter_shift, encode_or_decode=direction)

    final=  input("Do you want to keep going? Type yes or no.\n")

    if final == "no":
        should_continue = False
        print("thanks for playing!")