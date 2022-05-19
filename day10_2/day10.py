from art import logo


def add (n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2) :
    return n1/n2

operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/": divide 
}


def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?\n"))
    for sign in operations:   
        print(sign)
        should_continue = True

    while  should_continue:
        
        sign_op = input("which sign do you want to use?\n")
        num2 = float(input("What's your next number?\n"))
        calculation_function = operations[sign_op]
        answer = calculation_function(num1,num2)
        print(f"{num1} {sign_op} {num2} = {answer}")
        
        repeat = input(f"Type 'y' to continue calcualting with {answer}, or type 'n' to start a new calculation or type 'exit' to stop \n" )
        if repeat == 'y':
            num1 = answer
        
        elif repeat =='n':
            should_continue = False
            
            calculator()
        elif repeat == 'exit':
            print('goodbye')
            break
        else:
            print('invalid input, try again')
        
calculator()
                