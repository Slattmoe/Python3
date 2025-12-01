# Imported the logo from art.py
import art
logo = art.logo
print(logo)

# Created a function to find the highest bidder
def highestbid(dictionary):

    # Created empty int here to store the highest bidder
    highestbid = 0

    # Created empty string to store what key we are on
    winner = ''

    # Created a forloop that loops through wtv dictionary we decide to read when we call this function
    for i in dictionary:
        # inside the loop: if the highest bid is less than our value at the current key
        if highestbid < dictionary[i]:
            # highest bid is now what ever that value is, and winner is where that key is at the given time!
            highestbid = dictionary[i]
            winner = i
    print(f"The winner is {winner} with a bid of ${highestbid}")


# Created an empty dictionary here to store the names and grades
auction = {}

# Got user input here
name = input("What is your name? ").lower()
bid = int(input("What is your bid? $"))

# Created a new key called name with the value bid
auction[name] = bid

# Asking if they'd like to sumbit more bids
continuebid = input("Are there any other bidders? yes or no: ")

# Created variable to check against the while loop
bidcon = True

# While loop
while bidcon:
    # IF statement checking if the user wants to input more bids, getting and storing their inputs into the auction
    if continuebid == 'yes':
        name = input("What is your name? ").lower()
        bid = int(input("What is your bid? $"))
        auction[name] = bid
    
    # Asking if they'd like to continue
        continuebid = input("Are there any other bidders? yes or no: ")
    # The core function of the program!!!
    # Comparing the values in the auction using the function we created. Makes it more simple. instead of writing this out
    else:
        highestbid(auction)
        bidcon = False

