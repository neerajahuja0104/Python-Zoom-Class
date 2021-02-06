# TASK_1

# 1
a, b, c = 1, 2.01, "string"
print(a, b, c)


# 2
a, b = 1 + 2j, 5
print(a, b)
print(type(a))
print(type(b))
a, b = b, a
print(a, b)
print(type(a))
print(type(b))


# 3
# with 3rd variable
a, b = 3, 7
c = a
a = b
b = c
print(a, b)
# with just 2 variables
a, b = 2, 8
a, b = b, a
print(a, b)


'''# 4
i = input("Enter input to print: ")
print(i)'''


# 5
a, b = int(input("Enter a numbers between 1-10: ")), int(input())
if 0 < a < 11 and 0 < b < 11:
    z = a + b
    result = z + 30
    print("Final output: ", result)
else:
    print("One or more entered number does lies between 1-10")


# 6
a = eval(input("Enter input in proper format to get type output: "))
print("The data type of the input value is: ", type(a))


# 7
UpperCamelCase = "This is also known as PascalCase"
lowerCamelCase = "This one is lowerCamel"
snake_case = "This one is snake_case"
UPPERCASE = "THIS ONE IS UPPERCASE"
print(UpperCamelCase)
print(lowerCamelCase)
print(snake_case)
print(UPPERCASE)


# 8
# Yes, it will change the value. A Python variable's name is a key in the
# global (or local) namespace, which is effectively a dictionary.
# The underlying value is some object in memory. Assignment gives a name to that object.
# Re-assignment of one variable changes what object is named by that variable.