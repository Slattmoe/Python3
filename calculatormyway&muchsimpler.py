
def calculator():
    """ Created a calculator!"""

    # Functions to calculate
    def add(a, b):
        return a + b

    def substract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    # Got the users input here
    firstnumber = int(input("What's your first number?: "))

    # Printed the choices of operations
    print("+\n-\n*\n/\n")

    # got the users choice
    operation = input("Pick an operation: ")

    # got the second number
    secondnumber = int(input("What's the next number?: "))

    # stored it in a dictionary which made it super easy to access
    calculations = {"+": add(firstnumber, secondnumber), "-": substract(firstnumber, secondnumber),
                    "*": multiply(firstnumber, secondnumber), "/": divide(firstnumber, secondnumber), }

    # Conditional to test what operation user picked!
    if operation == "+":
        return calculations["+"]
    elif operation == "-":
        return calculations["-"]
    elif operation == "*":
        return calculations["*"]
    elif operation == "/":
        return calculations["/"]
    # Validating user input
    else:
        return "You didn't enter a valid operator, please rerun the program"


print(calculator())
