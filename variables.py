# working with string
phrase = "Python Programming"
print(phrase.isupper())  # result boolean false
print(phrase.upper().isupper())  # result boolean true because 1st it transforms into uppercase
print(len(phrase))  # count length
print(phrase[1])  # python always start from zero
print(phrase.index("r"))  # find the index of string - note case-sensitive
print(phrase.index("Py"))  # find the index of string start
print(phrase.replace("Programming", "Project"))
