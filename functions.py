import random
def greet(name):
    print(f'Hi! {name}')
    print("\nWelcome to the number guessing game!!!")
    
greet("Mahad")

# created the secret number the computer number will guess
secret = random.randint(1, 10)

# Getting the users pick here
pick = int(input("what is your pick: 1-10: "))

# Validating the users pick here, only checks the initial pick
if pick > 10 or pick < 1:
    print("invalid input please enter right value")


# Created a while loop to test if user's pick was right
while pick != secret:
    # Validating the users input after they run it a second time!
    if pick > 10 or pick < 0:
        print("invalid input, please run the program again")
        break
    print(f"\nyour pick was: {pick}")
    print("Wrong guess sorry\n")
    # Printed the computers guess 
    print(f"the right guess was: {secret}")
    # Updated the condition in here | still in the while loop though!!
    secret = random.randint(1, 10) 
    pick = int(input("pick again: "))
if pick == secret:
    print(f"\nyour pick was: {pick}")
    print(f"\nthe right guess was: {secret}")
    print("\ncongrats you finally guessed right!!")
