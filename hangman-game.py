word_list = ["aardvark" , "camel" , "baboon", "monkey"]
stages = ["ouch", "ugh", "ee", "ump", "nor", "goop"]

import random
chosen_word = random.choice(word_list)
placeholder = ""

length =len(chosen_word)
lives = 6


for position in range(0, length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter\n").lower()

    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

        if guess in correct_letters:
            print("you already guessed that!")
    if guess not in correct_letters:
        lives -= 1
        print(f"you have {lives} lives left")

    print(display)
   

    if "_" not in display:
        game_over = True
        print("!!!!!!!!!!!!!!!!!!!!You win!!!!!1111111!!!1111!!")
    elif lives == 0:
        game_over = True
        print(";-; you lose (\\\_-) ")
    


