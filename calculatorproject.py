import art

logo = art.logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculations():
    shouldcontinue = True
    while shouldcontinue:
        firstnumber = int(input("What is your first number?: "))
        for i in operations:
            print(i)
        operator = input("Pick an operator from the above: ")
        secondnumber  = int(input("What is your second number?: "))
        answer = operations[operator](firstnumber, secondnumber)
        print(f'{firstnumber} {operator} {secondnumber} = {answer}')

        continued = input("Would you like to continue? Type y or n: ")
    
        if continued == 'y':
            firstnumber = answer
        else:
            shouldcontinue = False
            print("\n" * 20)
            return "Good Bye"

print(calculations())
