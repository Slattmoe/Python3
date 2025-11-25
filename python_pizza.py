print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
size = size.upper()  # force uppercase
bill = 0 # created a variable with the bill

if size == "S": # if the size is small, bill becomes 15
    bill += 15
elif size == "M": # if the size is medium, bill becomes 20
    bill += 20
elif size == "L": # if the size is large, bill become 25
    bill += 25
else: # if the user enters something else other than those 3
    print("You entered a different char other than S, M, or L")
    quit()  # uncomment this if you want to exit

pepperoni = input("Do you want pepperoni? Y or N ") ## created var for the pepperoni codition
pepperoni = pepperoni.upper()

if pepperoni == "Y": # if the user wanted pepperoni
    if size == "S": # if the size was small then we
        bill += 2
    elif size in ["M", "L"]:
        bill += 3

cheese = input("Do you want cheese on your pizza? Y or N ")
cheese = cheese.upper()

if cheese == "Y":
    bill += 1
elif cheese == "N":
    pass   # do literally nothing
print(f"Your final bill is: ${bill}.")



#                                                              This is the logic for this project!!!!
#  ┌──────────────────────────────────────┐
#  │      START: Welcome Message          │
#  └───────────────┬──────────────────────┘
#                  │
#                  ▼
#      ┌──────────────────────────────┐
#      │ Ask: Pizza Size (S/M/L?)     │
#      └───────────────┬──────────────┘
#                      │
#      ┌───────────────┼────────────────────────┐
#      ▼               ▼                        ▼
#  ┌────────┐     ┌──────────┐            ┌──────────┐
#  │ Size=S │     │ Size=M   │            │ Size=L   │
#  └─────┬──┘     └─────┬────┘            └─────┬────┘
#        │              │                     │
#        ▼              ▼                     ▼
#   bill +=15      bill +=20             bill +=25
#        │              │                     │
#        └──────────────┴────────────┬────────┘
#                                    │
#                                    ▼
#                      ┌─────────────────────────┐
#                      │ Invalid size entered?   │
#                      └───────────────┬─────────┘
#                                      │YES
#                                      ▼
#                            ┌──────────────────┐
#                            │ Print error       │
#                            │ and QUIT          │
#                            └──────────────────┘
#                                      │NO
#                                      ▼
#                    ┌────────────────────────────────┐
#                    │ Ask: Pepperoni? (Y/N)          │
#                    └─────────────────┬──────────────┘
#                                      │
#                                      ▼
#                          ┌────────────────────┐
#                          │ pepperoni == "Y"?  │
#                          └───────┬────────────┘
#                                  │YES
#                                  ▼
#                       ┌────────────────────────────┐
#                       │ Is size S?                 │
#                       └──────────┬─────────────────┘
#                                  │
#                 ┌────────────────┼───────────────┐
#                 ▼                ▼               ▼
#           bill+=2        bill+=3 (M or L)       (else)
#                 │                │               │
#                 └────────────────┴───────────────┘
#                                      │
#                                      ▼
#                   ┌────────────────────────────────┐
#                   │ Ask: Cheese? (Y/N)             │
#                   └─────────────────┬──────────────┘
#                                     │
#                                     ▼
#                          ┌────────────────────┐
#                          │ cheese == "Y"?     │
#                          └──────┬─────────────┘
#                                 │YES
#                                 ▼
#                            bill +=1
#                                 │
#                                 ▼
#                        ┌────────────────────────┐
#                        │  FINAL: Print bill     │
#                        └────────────────────────┘