print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

lefttoright = input("Which direction do you want to go? Left or Right? ")
lefttoright = lefttoright.upper()

if lefttoright == "LEFT":
    swimorwait = input("Do you want to swim or wait? Pick one ")
    swimorwait = swimorwait.upper()
    if swimorwait == "WAIT":
        door = input("pick a door color: Red, Blue, or Yellow: ")
        door = door.upper()
        if door == "YELLOW":
            print("You win!!!")
            quit()
        elif door == "BLUE":
            print("You were eaten by beasts! GAME OVER")
            quit()
        elif door == "RED":
            print("You were burned in a fire! GAME IS OVER")
            quit()
    elif swimorwait == "SWIM":
        print("Attacked by trout! Game OVER")
elif lefttoright == "RIGHT":
    print("You fell into a hole! GAME OVER!")
    quit()
