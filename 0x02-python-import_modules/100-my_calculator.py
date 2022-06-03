#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    len_args = len(args)
    if len_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1 = int(args[1])
    num2 = int(args[3])
    op_passed = args[2]
    operator = ['+', '-', '*', '/']
    if op_passed not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op_passed == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif op_passed == '-':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif op_passed == '*':
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif op_passed == '/':
        print(f"{num1} / {num2} = {div(num1, num2)}")
