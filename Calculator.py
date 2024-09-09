# Basic calculator, takes 2 numbers and an operator and performs calculation

def main():
    number1 = input("Enter number: ")
    number2 = input("Enter another number: ")
    operand = input("Enter an operand +, -, *, /: ")
    calculator(number1, number2, operand)
    eval_function(number1, number2, operand)


def calculator(number1, number2, operand):
    print("calculator:")
    if number1.isdecimal() and number2.isdecimal():
        if operand == "+":
            calculation = int(number1) + int(number2)
        elif operand == "-":
            calculation = int(number1) - int(number2)
        elif operand == "*":
            calculation = int(number1) * int(number2)
        elif operand == "/":
            if int(number2) != 0:
                calculation = int(number1) / int(number2)
            else:
                calculation = "Error: cannot divide by zero"
        else:
            calculation = "Error: Invalid operator"
    else:
        calculation = "Error: Input must be a numeric value"

    output(calculation)


def output(calculation):
    print(calculation)


def eval_function(number1, number2, operand):
    # showcase the eval function but don't worry about error handling
    print("eval_function:")
    command = number1 + operand + number2
    result = eval(command)
    output(result)


main()
