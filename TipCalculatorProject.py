# Greet the user
print("Welcome to the tip calculator!")

# Ask for the total bill and convert the input to a float (decimal number)
bill = float(input("What was the total bill? $"))

# Ask the user what percentage tip they want (10, 12, or 15)
# int() because the user enters whole numbers
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people will split the bill
# int() because number of people is whole numbers
people = int(input("How many people to split the bill? "))

# Convert the tip percentage to a multiplier
# Example: 12 percent -> 12/100 = 0.12, so multiplier = 1.12
tip_multiplier = 1 + (tip_percent / 100)

# Calculate each person's share including tip
# First divide the bill by number of people, THEN add the tip multiplier
subtotal = (bill / people) * tip_multiplier

# Round to 2 decimal places so it looks like real currency
total_rounded = round(subtotal, 2)

# Display the final amount each person pays
print(f"Each person pays ${total_rounded}")
