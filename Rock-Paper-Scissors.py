rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)
nplayer_choice = int(player_choice)

if nplayer_choice == 0:
  print(rock)
if nplayer_choice == 1:
  print(paper)    
if nplayer_choice == 2:
  print(scissors)


print("Computer chose:")
if computer_choice == 0:
    print(rock)
if computer_choice == 1:
    print(paper)
if computer_choice == 2:
    print(scissors)

if nplayer_choice == 0 and computer_choice == 0:
    print("Draw")
if nplayer_choice == 0 and computer_choice == 1:
    print("You lose")
if nplayer_choice == 0 and computer_choice == 2:
    print("You win")
if nplayer_choice == 1 and computer_choice == 0:
    print("You win")
if nplayer_choice == 1 and computer_choice == 1:
    print ("Draw")
if nplayer_choice == 1 and computer_choice == 2:
    print("You Lose")
if nplayer_choice == 2 and computer_choice == 0:
    print("You lose")
if nplayer_choice == 2 and computer_choice == 1:
    print("You win")
if nplayer_choice == 2 and computer_choice == 2:
    print("Draw")