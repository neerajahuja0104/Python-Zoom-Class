# TASK 5

# 1
def synerr():
    try:
        break
    except SyntaxError:
        print("Syntax is not right. Please check and try again.")
    return 0


# 2
import sys
i1 = (input("Enter a name for file: "))
with open(sys.argv[0], 'r') as f:
    if sys.argv[0] != i1:
        raise NameError("Please enter the name again.")


# 3
i2 = (input("Enter a four digit number: "))
if len(i2) != 4:
    raise Exception("The length is too short/long !!! Please provide only four digits")


# 4
i6 = 4
while i6 > 0:
    i3 = input("Enter username: ")
    i4 = input("Enter password: ")
    i5 = input("Re-type password: ")
    if i4 != i5:
        i6 = i6 - 1
        print("You have", i6, "chances remaining !")
    else:
        print("You have entered your space.")
        break
if i6 == 0:
    raise Exception("Account locked. Please try again after 24 hours.")'''


# 6
'''a = open("doc.txt", "wt")
a.write("Hello I am a file\nWhere you need to return the data string\nWhich is of even length\nMake sure you return the content in The same link as it is present.")
a.close()

a = open("doc.txt", "rt")
a1 = a.read()
a2 = a1.split('\n')
for a3 in a2:
    if len(a3) % 2 == 0:
        print(a3, len(a3))
