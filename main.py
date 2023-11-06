from lexer import Lexer
from my_parser import Parser
from interpreter import Interpreter

while True:
    try:
        first_num = float(input("Enter the first number: "))
        operator = input("Enter an operator (+ or -): ")
        second_num = float(input("Enter the second number: "))

        if operator not in ("+", "-"):
            print("Invalid operator. Please enter + or -.")
            continue

        if operator == "+" and second_num < 0:
            second_num = abs(second_num)
            operator = "-"
        elif operator == "-" and second_num < 0:
            second_num = abs(second_num)
            operator = "+"

        text = f"{first_num} {operator} {second_num}"
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {str(e)}")

    user_input = input("Do you want to continue (yes/no)? ").lower()
    if user_input != "yes":
        break