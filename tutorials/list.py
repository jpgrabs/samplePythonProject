print("--List Tutorial--")
colorList = ["Red", "Yellow", "Blue", "Green", "Pink", "Pink", "Pink"]
colorList[0] = 'Black'
print(colorList)
print(colorList[2])  # select specific index value
print(colorList[-2])  # select specific index on negative value
print(colorList[1:3])  # select value on specific range
print(colorList[0])  # modify on selected index list
print("----------------")
print("--List Function Tutorial--")
colorList.append("Orange")  # Add another on original list
print(colorList)
random_number = [2, 9, 6, 9, 27, 11, 29]
colorList.extend(random_number)  # combine with another number
print(colorList)
colorList.insert(1, "Violet")  # inset item before the selected index
print(colorList)
colorList.remove("Violet")  # inset item before the selected index
print(colorList)
# colorList.clear()  # easily remove the last element on the list
# print(colorList)
# colorList.pop()  # show the list
# print(colorList)
print(colorList.index("Blue"))  # find and show index value - note case-sensitive
print(colorList.count("Pink"))  # find and count how many value in the list
colorListPro = ["Red", "Yellow", "Blue", "Green", "Pink", "Pink", "Pink"]
colorListPro.sort()  # arrange in ascending order
print(colorListPro)
random_number.sort()  # arrange in ascending order
print(random_number)
random_number.reverse()  # arrange in descending order
print(random_number)
colorListPro2 = colorListPro.copy()  # copy the list variables into new list
print(colorListPro2)
