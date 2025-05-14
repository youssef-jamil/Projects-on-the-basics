# the challenge number three Define function called calculate
# given three number will return add the first two numbers and multiply the third number
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))


def calculate(num1, num2, num3):
    return (num1 + num2) * num3


# ! the calling the function
calculate(num1, num2, num3)
calculate(num1, num2, num3)

print(f"The result is = {calculate(num1 , num2 , num3)}")
