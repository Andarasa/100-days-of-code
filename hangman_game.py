word_list = ["aardvark" , "camel" , "baboon"]

import random
chosen_word = random.choice(word_list)
placeholder = ""
display = ""
length =len(chosen_word)

print(chosen_word)
print(placeholder)

for position in range(0,):
    placeholder += "_"

guess = input("Guess a letter\n").lower()
print(guess)

for letter in chosen_word:
    if guess == letter:
        print("right!")
        display = placeholder.replace(letter,guess)
    elif guess != letter:
        print("wrong!")

print(display)