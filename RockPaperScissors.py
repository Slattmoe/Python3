import random

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

# Created a list with the 3 choices
computer_choice = [rock, paper, scissors]

#Greeted users
print("!!!  Welcome to the rock, paper, scissors game  !!!")

#stored the users pick in a int 
user_pick = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))

# Validate input
if user_pick < 0 or user_pick > 2:
    print("Invalid choice.")
    quit()

# Show user's choice
print("You chose:\n" + computer_choice[user_pick])

# Computer picks
comp_pick = random.choice(computer_choice)

print("\nComputer chose:\n" + comp_pick)

# Game logic
if user_pick == 0:       # rock
    if comp_pick == 1:
        print("\nYou lose.")
    elif comp_pick == 2:
        print("\nYou win!")
    else:
        print("\nIt's a tie.")

elif user_pick == 1:     # paper
    if comp_pick == 2:
        print("\nYou lose.")
    elif comp_pick == 0:
        print("\nYou win!")
    else:
        print("\nIt's a tie.")

elif user_pick == 2:     # scissors
    if comp_pick == 0:
        print("\nYou lose.")
    elif comp_pick == 1:
        print("\nYou win!")
    else:
        print("\nIt's a tie.")

