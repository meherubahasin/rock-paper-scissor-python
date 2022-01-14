
#File Name: main.py                       
#Description: A Rock, Paper and Scissor game project

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

import random

gameimages = [rock, paper, scissors]

userchoice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computerchoice = random.randint(0, 2)

print("\n")

print("You chose:\n")
if userchoice >= 3 or userchoice < 0:
  print("Invalid number!")
else:
  print(gameimages[userchoice])

print("\n")

print(f"Computer chose:\n")
print(gameimages[computerchoice])



if userchoice == computerchoice:
  print("Draw.")

#losing conditions
elif userchoice == 1 and computerchoice == 2:
  print("You lose.")
elif userchoice == 0 and computerchoice == 1:
  print("You lose.")
elif userchoice == 2 and computerchoice == 0:
  print("You lose.")
elif userchoice >= 3 or userchoice < 0:
  print("You lose.")

#wining conditions
elif userchoice == 2 and computerchoice == 1:
  print("You win.")
elif userchoice == 1 and computerchoice == 0:
  print("You win.")
elif userchoice == 0 and computerchoice == 2:
  print("You win.")
