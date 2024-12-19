# match case calc
#prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#prompt the user to choose an operation
operation = input("choose the operation (+,-,*,/): ").strip()

#perform the calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1-num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result =  num1 / num2
            print(f"The result is {result}.")
        else:
            print("cannot divide by Zero.")
    case _:
        print("Invalid operation. Pease choose one of +, -, *, or /.")
