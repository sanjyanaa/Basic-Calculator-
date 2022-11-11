
#building a calculator
number1 = float(input("Insert a number:"))
operator= input("Enter your operation sign:")
number2 = float(input("Insert a number:"))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "%":
    print(number1 % number2)
else:
    print("Invalid entry")




