# TASK 2

# 1
i = int(input("Enter a natural number: "))

if i % 3 == 0 and i % 5 == 0:
    print("Consultadd - Python Training")
elif i % 3 == 0:
    print("Consultadd")
elif i % 5 == 0:
    print("Python Training")
else:
    print("Entered natural number is neither divisible by 3 or 5")


# 2
print("Following are the options available - 1: Addition, 2: Subtraction, 3: Division, 4: Multiplication, 5: Average")

i = int(input("Select a SINGLE option from ones listed above: "))
num1, num2 = int(input("Enter 2 numbers: ")), int(input())
total = 0

if i == 1:
    total = num1+num2
if i == 2:
    total = num1-num2
if i == 3:
    total = num1/num2
if i == 4:
    total = num1*num2
if i == 5:
    first, second = int(input("Enter 2 more numbers for average operation: ")), int(input())
    total = (num1 + num2 + first + second) / 4

print(total)
if total < 0:
    print("NEGATIVE")


# 3
a, b, c = 10, 20, 30
avg = (a+b+c)/3
print("avg = ", avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a, b and c")
elif avg > a and avg > b:
    print("avg is higher than a and b")
elif avg > a and avg > c:
    print("avg is higher than a and c")
elif avg > b and avg > c:
    print("avg is higher than b and c")
elif avg > a:
    print("avg is higher than a")
elif avg > b:
    print("avg is higher than b")
elif avg > c:
    print("avg is higher than c")
else:
    print("avg is lower than a, b and c")


# 4
i = 1

while i >= 0:
    x = input("Do you want to enter the process (Y/N): ")

    if x == 'Y':
        i = int(input("Enter an integer (positive or negative): "))
        if i > 0:
            print("Good Going")
            continue
        elif i < 0:
            print("It's Over")
            break
        elif i == 0:
            print("You entered zero")
        else:
            print("J")
    elif x == 'N':
        print("Thank you for your time")
        break
    else:
        print("Please enter a value from Y/N")


# 5
print("These are numbers between 2000 and 3200 which are divisible by 7 but are not multiples of 5: ")
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=" ")


# 6
print("#1: for i in x:\nTypeError: 'int' object is not iterable")

print("#2: 0\nerror\n1\nerror\n2")

print("#3: Break NameError: name 'Break' is not defined\n0\n1\n2\n3\n4")


# 7
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)


# 8
i = (input("Enter any alphanumeric string: "))
L, d, u = 0, 0, 0
for x in i:
    if x.isdigit() == 1:
        d += 1
    elif x.isalpha() == 1:
        L += 1
    else:
        u += 1
print("Letters ", L, "Digits ", d, "Special characters ", u)


# 9
i = 0
while i != 7:
    i = int(input("Guess the lucky number between 1-10: "))
    if i == 7:
        print("Success! you guessed the lucky number.")
        break
    elif i < 1 or i > 10:
        print("Please enter a guess within the range.")
    else:
        print("Sorry, wrong guess. Please try again.")

i = 0
while i != 7:
    answer = input("Do you want to play guess (yes/no): ")
    if answer == 'yes':
        i = int(input("Guess the lucky number between 1-10: "))
        if i == 7:
            print("Success! you guessed the lucky number.")
            break
        elif i < 1 or i > 10:
            print("Please enter a guess within the range.")
        else:
            print("Sorry, wrong guess.")
    elif answer == 'no':
        print("Thank you.")
        break
    else:
        print("Please enter a proper response from yes or no.")


# 10
counter = 1
while counter <= 5:
    print("Type in the", counter, "number (1-10): ")
    counter = counter + 1
    i = int(input())
    if i == 7:
        print("Good guess!")
    elif i < 1 or i > 10:
        print("Please enter a guess within the range.")
    else:
        print("Try again!")
print("Game over!")


# 11
i = 0
counter = 1
while counter <= 5:
    print("Type in the", counter, "number (1-10): ")
    counter = counter + 1
    i = int(input())
    if i == 7:
        print("Good guess!")
        break
    elif i < 1 or i > 10:
        print("Please enter a guess within the range.")
    else:
        print("Try again!")
if i != 7:
    print("Sorry but that was not very successful.")
