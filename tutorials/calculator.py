# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result1 = num1 + num2  # combine only two string
# print(result1)
#
# # result2 = int(num1) + int(num2)  # convert string into integers or whole number only
# # print(result2)
#
# result3 = float(num1) + float(num2)  # convert string into decimal
# print(result3)

# Building a better calculator
num1 = float(input("Enter 1st number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

