# working with string
# phrase = "Python Programming"
# print(phrase.isupper())  # result boolean false
# print(phrase.upper().isupper())  # result boolean true because 1st it transforms into uppercase
# print(len(phrase))  # count length
# print(phrase[1])  # python always start from zero
# print(phrase.index("r"))  # find the index of string - note case-sensitive
# print(phrase.index("Py"))  # find the index of string start
# print(phrase.replace("Programming", "Project"))

# working with numbers
print(2)
print(2.3)
print(-2.3)
print(2.3 + 5)  # python can do arithmatic operation
print(2 * (5 + 5))
print(10 % 3)

var_number = 2
print(var_number)
print(str(var_number) + " is the selected number")  # converted into string, python not allowed number & string

print(abs(var_number))  # absolute value number
print(pow(3, 2))  # 3 ^2 or 3 raise power of 2
print(min(3, 6))  # find the lowest number on between range
print(max(3, 6))  # find the highest number on between range
print(round(4.7))  # rounding the number : 3,4 = 3 and 3.6 = 4
print(round(4.4))  # rounding the number : 3,4 = 3 and 3.6 = 4

from math import *
# import python math and give us lot more math function
print(floor(4.7))  # just grab the lowest number
print(ceil(4.7))  # round out the number
print(sqrt(36))  # square root of the number
