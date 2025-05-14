# create module withe 4 operations
# ! This program takes three variables from you,
#! two of them are numbers and the third is the operation that gets the two numbers.
#! You have three attempts if the operation is invalid.
# ? accept 3 inputs from the user
# ? use Math module from python (pow and sqrt)
# ? Import random2 from pypi
from python3 import modulChallenge
import math
import random2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator:(+,-,*,/,pow,sqrt) ")

if operator == "+":
    result = modulChallenge.add(num1, num2)
elif operator == "-":
    result = modulChallenge.subtract(num1, num2)
elif operator == "*":
    result = modulChallenge.multiply(num1, num2)
elif operator == "/":
    result = modulChallenge.divide(num1, num2)
elif operator == "pow":
    result = math.pow(num1, num2)
elif operator == "sqrt":
    result = math.sqrt(num1)
elif operator == "random":
    result = random2.randint(num1, num2)
else:
    counter = 0
    while counter < 3:
        print(
            f"return Enter the coorct operator please & you have {3 - counter} chance"
        )
        operator = input("Enter operator: ")
        if operator == "+":
            result = modulChallenge.add(num1, num2)
            break
        elif operator == "-":
            result = modulChallenge.subtract(num1, num2)
            break
        elif operator == "*":
            result = modulChallenge.multiply(num1, num2)
            break
        elif operator == "/":
            result = modulChallenge.divide(num1, num2)
            break
        elif operator == "pow":
            result = math.pow(num1, num2)
            break
        elif operator == "sqrt":
            result = math.sqrt(num1)
            break
        elif operator == "random":
            result = random2.randint(num1, num2)
        else:
            result = "Invalid operator"

        counter += 1
        if result == "Invalid operator" and counter == 3:
            break

print(f"The result by the operator {operator} is: {result}")
if result == "Invalid operator":
    print("You have reached the maximum number of attempts")
