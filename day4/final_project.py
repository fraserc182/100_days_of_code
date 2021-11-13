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
import time

computer_choice = random.randint(0,2)
choice_list = ["rock", "paper", "scissors"]

print("Welcome to rock, paper, scissors")
time.sleep(0.5)
print(rock)
time.sleep(0.5)
print(paper)
time.sleep(0.5)
print(scissors)
time.sleep(1)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("")

if user_choice >= 3 or user_choice < 0:
    print("Invalid number, try again!")
elif user_choice == 0 and computer_choice == 2:
  print(f"You win!\n{choice_list[user_choice]} beats {choice_list[computer_choice]}")
elif computer_choice > user_choice:
  print(f"You lose!\n{choice_list[computer_choice]} beats {choice_list[user_choice]}")
elif user_choice == computer_choice:
  print(f"Game is a draw!\nBoth players chose {choice_list[computer_choice]}")
else:
  print(f"You win!\n{choice_list[user_choice]} beats {choice_list[computer_choice]}")

