print("!!! Welcome to the roalercoaster game by: Mahad !!!")

height = int(input("What is your height? ")) # Created a var for the height here
bill = 0 # created a var for the bill here and set it to 0

if height >= 120:                               # testing the first condition: if their height is greater than or equal to 120 cm
    print("You can ride the roalercoaser")                     # if the first condition is true then we ask the user for their age      
    age = int(input("What is your age? "))                  # asking user for the age and put it in the age var
    if age <= 12:                                   # this is where i was going wrong (I was doing if age was greater than 12 or equal to 12, which was just defaulting to 5)
        bill += 5       # if their age is 12: the price is 5$
    elif age >= 13 and age <= 18:       # second conditions being tested using the AND method. if age is greater than 13(or equal to), AND if the age is smaller than 18 or equal= price: 7
        bill += 7
    elif age > 19: # if user is older than 19, the price is 12$
        bill += 12
    picture = input("Do you want a picture? Y or N: ")  # before the if statement ends, we ask the user one last question, do they want pics, if so we do another if else statement!
    if picture == "Y":
        bill += 3
        print(f"Your total is {bill}")
    elif picture == "N":
        print(f"Your total is {bill}")
        quit()                  # totally unnecessary right now!
else: 
    print("sorry you're too short")