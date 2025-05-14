#! the Calculator Application
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the type of operator (+,-,*):")
# ! the input function is used to take input from the user
# ! the (f"") is a formatting to string in the print function

if operator == "+":
    print(f"{num1} + {num2} = {(num1) + (num2)}")
elif operator == "-":
    print(f"{num1} - {num2} = {(num1) - (num2)}")
elif operator == "*":
    print(f"{num1} * {num2} = {(num1) * (num2)}")
else:
    print("We don't support this operator,Supported operations are: +, -, *")

print("Thanks for using the Calculator")
