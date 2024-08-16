
def encrypt():
    original_text = input("What message do you want to encode?")
    letter_shift = input("How many letters do you want to shift by?")

    alphabet = ["a" , "b" , "c", "d", "e", "f", "g", "h", "i", "J", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in original_text:
            