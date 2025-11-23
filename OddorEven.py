fav_number = int(input("what's your favorite number: "))

num_check = fav_number % 2

if num_check == 1:
    print("your number is odd!")
elif num_check == 0:
    print("your number is even!")
