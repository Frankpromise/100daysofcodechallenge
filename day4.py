import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
games_image = [rock, paper, Scissors]
user_choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n'))
print(games_image[user_choice])

computer_choice = random.randint(0,2)
print(f'Computer choose:{computer_choice}')
print(games_image[user_choice])

if user_choice == 0 and computer_choice == 2:
    print('You win!')
elif user_choice > computer_choice:
    print('You win')
elif computer_choice > user_choice:
    print('You lose!')
elif user_choice == computer_choice:
    print('It is a draw!')
elif computer_choice < user_choice:
    print('You lose!')
else:
     print('invalid input! you lose.')
