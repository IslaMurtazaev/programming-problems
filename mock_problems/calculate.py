# You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of non-negative integers.

# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample output:
#   calculate("5+16-((9-6)-(4-2))+1") => 21
#   calculate("22+(2-4)") => 20
#   calculate("6+9-12") => 3
#   calculate("((1024))") => 1024
#   calculate("1+(2+3)-(4-5)+6") => 13
#   calculate("255") => 255

# n: length of the input string

"""
6+9-12 => 15 - 12 => 3
22+(2-4) => 22 + -2 => 20

try to recursively break down the problem to single operation

if we find an opening parenthesis call our recursive function
to solve what ever expression lies inside parentheses and return single value
"""

def calculate(expression):
    num1 = ""
    num2 = ""
    operator = None

    open_parentheses = 0
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            open_parentheses += 1
        if expression[i] == ')':
            open_parentheses -= 1


        if expression[i] in ('+', '-'):
            operator = expression[i]





