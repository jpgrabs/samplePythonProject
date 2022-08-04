
# is_male = True
# is_tall = False
#
# if is_male or is_tall:
#     print("You are male or tall or both")
# else:
#     print("You neither Male nor tall")

is_male1 = False
is_tall1 = True

if is_male1 and is_tall1:
    print("You are tall male")
elif is_male1 and not is_tall1:
    print("You are short Male")
elif not is_male1 and is_tall1:
    print("You are not a Male but tall")
else:
    print("You are either not male or not tall or both")
