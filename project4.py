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
0 == rock
1 == paper
2 == scissors
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choice = random.randint(0, 2)
if my_choice == 0 and computer_choice == 2:
  print("You win.")
elif my_choice == 0 and computer_choice == 1:
  print("You lose.")
elif my_choice == 1 and computer_choice == 0:
  print("You win.")
elif my_choice == 1 and computer_choice == 2:
  print("You lose.")
elif my_choice == 2 and computer_choice == 0:
  print("You lose.")
elif my_choice == 2 and computer_choice == 1:
  print("You win.")
elif my_choice == computer_choice:
  print("Draw")