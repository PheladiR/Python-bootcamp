logo = """_____________________
|  _________________  |
| | PO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(n1,n2):
    return n1+n2


def subtract (n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {"+": add,"-": subtract, "*":multiply, "/": divide}


##########################



def calculations():
    should_accumulate = True
    print(logo)
    num1= float(input("Please type the first number:\n"))
    
    while should_accumulate:
        for symbol in operations:
           print(symbol)
        operation = input("Which operation are you choosing:\n")
        num2 = float(input("Please type the second number:\n"))
        result = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        choice = input(f"Do you wish to continue with {result}? Type 'y' for yes and 'n' for no:\n")
        
        if choice == "y":
           num1 = result
        else:
            should_accumulate = False
            print("\n" *20)
            calculations()  

        
calculations()


