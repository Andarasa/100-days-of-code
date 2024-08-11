word_list = ["aardvark" , "camel" , "baboon"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter\n").lower()
print(guess)

for letter in chosen_word:
    if guess == letter:
        print("right!")
    elif guess != letter:
        print("wrong!")