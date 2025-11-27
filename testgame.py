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
## Greet the user

print("Welcome to the rock paper scissors game")

# make a list the computer can parse

computerchoice = [rock, paper, scissors]
# Get user input

userchoice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors: "))


# indexed the users choice based on the list 
userpick = computerchoice[userchoice]

# print users choice 

if userpick == rock:
    print(rock)
elif userpick == paper:
    print(paper)
elif userpick == scissors:
    print(scissors)
else:
    print("invalid value")
    quit()


# computers pick
computerpick = random.choice(computerchoice)

# print the computers pick

if computerpick == rock:
    if userpick == paper:
        print("you won")
    elif userpick == scissors:
        print("you lose")
    else:
        print("it's a tie")
    print(rock)
elif computerpick == paper:
    if userpick == scissors:
        print("you won")
    elif userpick == rock:
        print("you lose")
    else:
        print("it's a tie")
    print(paper)
elif computerpick == scissors:
    if userpick == rock:
        print("you won")
    elif userpick == paper:
        print("you lose")
    else:
        print("it's a tie")
    print(scissors)

