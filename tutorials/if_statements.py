# is_male = True
# is_tall = False
#
# if is_male or is_tall:
#     print("You are male or tall or both")
# else:
#     print("You neither Male nor tall")

# is_male1 = False
# is_tall1 = True
#
# if is_male1 and is_tall1:
#     print("You are tall male")
# elif is_male1 and not is_tall1:
#     print("You are short Male")
# elif not is_male1 and is_tall1:
#     print("You are not a Male but tall")
# else:
#     print("You are either not male or not tall or both")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num3 >= num1:
        return num2
    else:
        return num3


input_num1 = input("Enter 1st num: ")
input_num2 = input("Enter 2nd num: ")
input_num3 = input("Enter 3rd num: ")

print(max_num(int(input_num1), int(input_num2), int(input_num3)))


def string_functions(str_color):
    if str_color == "Blue":
        print("You hair color is black and nice")
        return str_color
    elif str_color == "Red":
        print("You hair color is Red and you are beautiful")
        return str_color
    else:
        print("You hair color seems normal")
        return str_color


hair_color = input("Input your hair color: ")
print(string_functions(hair_color))



