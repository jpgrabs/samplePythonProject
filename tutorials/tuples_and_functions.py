# Tuples is a type of data structure which basically means container where can store different value
# Tuples is very similar to list top store multiple information in the list but different in lift function

coordinates = (4, 5)  # can't change and don't modify the list
print(coordinates[0])  # select specific index


# Basic Function Tutorial
# coordinates[1] = 10  # TypeError: 'tuple' object does not support item assignment
# print(coordinates)  # tuples is immutable because you can't change the list

# def means function in python, the function must be inside the indent function
print("----------------")
print("-- Basic Function Tutorial--")


def hello_world():
    name = input("Enter your name : ")
    print("Hello " + name)
    your_feeling = input("Are you feeling well today? : ")
    print(your_feeling + ", Wow that's great!")


print("--------")
hello_world()
print("--------")


def the_function(name, age):
    print("Hello " + name + " and you are " + age)


the_function("Python", "27")
the_function("Android", "29")


def the_function2(name, age):
    print("And also hello " + name + " and you are " + str(age))


the_function2("IOs", 11)

print("----------------")
print("-- Return Statement Tutorial--")


def cube(num):
    return num * num * num


print(cube(3))
result = cube(4)
print(result)

