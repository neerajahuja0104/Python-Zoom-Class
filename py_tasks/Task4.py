# TASK 4

# 1
def rev(a2):
    return a2[::-1]


b = input("Enter a string to reverse:")
c = rev(b)
print(c)


# 2
def ques2(d1):
    upr = 0
    lwr = 0
    for i1 in d1:
        if i1.isupper() == 1:
            upr += 1
        elif i1.islower() == 1:
            lwr += 1
    return upr, lwr


e = input("Enter a string with uppercase and lowercase letters: ")
f, g = ques2(e)
print("There are", f, "uppercase letters and", g, "lowercase letters.")


# 3
def unq(h):
    i2 = list(set(h))
    return i2


j = list(input("Enter redundant elements for a list in comma-separated manner:").split(','))
k = unq(j)
print(k)


# 4
n = input("Enter a hyphen-separated sequence of words: ").split('-')
n.sort()
print('-'.join(n))


# 5
print("Enter sequence of lines, press Enter to separate them and press Enter twice to end input:")
seq = []
while True:
    line = input()
    if line:
        LINE = line.upper()
        seq.append(LINE)
    else:
        break
caps = '\n'.join(seq)
print(caps)


# 6
def rec():
    a2, b1 = input("Enter integral values for a and b:"), input()
    c2 = int(a2)
    d3 = int(b1)
    sum_i = c2 + d3
    return sum_i


Sum = rec()
sum_s = str(Sum)
print("Sum for a and b is:", sum_s)


# 7
def prntstr():
    str1 = input("Enter one string:")
    str2 = input("Enter another string:")
    if len(str1) == len(str2):
        print(str1, "\n", str2, "\nare of equal lengths.")
    elif len(str1) > len(str2):
        print(str1, "is the larger string.")
    else:
        print(str2, "is the larger string.")
    return 0


a = prntstr()


# 8
def tup():
    d4 = []
    for a4 in range(1, 21):
        b3 = (lambda c3: c3*c3)
        d4.append(b3(a4))
    e2 = tuple(d4)
    return e2


x = tup()
print(x)


# 9
def shownumbers(limit):
    i3 = 0
    while i3 <= limit:
        if i3 % 2 == 0:
            print(i3, "EVEN\n")
        elif i3 % 2 != 0:
            print(i3, "ODD\n")
        i3 += 1
    return 0


x = int(input("Enter a value for limit parameter:"))
y = shownumbers(x)


# 10
c = list(range(1, 21))
aa = list(filter(lambda b5: (b5 % 2 == 0), c))
print("Even numbers in list for range 1-20 are:", aa)


# 11
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = list(filter(lambda b6: (b6 % 2 == 0), c))
d = list(map(lambda e4: (e4 * e4), A))
print("Sqaures of even numbers from", c, "are:", d)


# 12
def funcn():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("Cannot divide anything with zero")
    return 0


ab = funcn()


# 13
import functools
import operator
a1 = [1, 2, 3, 4, 5, 6, 7]
b = []
for i in a1:
    j = str(i)
    b.append(j)
print("The list after using reduce is: ")
print(functools.reduce(operator.add, b))


# 14
i = list(map(int, input("\nEnter the numbers with space in between: ").strip().split()))
x = list(filter(lambda a7: (a7 % 7 == 0 and a7 % 3 != 0), i))
print(x)


# 15
def mult(i4):
    return i4 * i4


b = list(map(int, input("\nEnter the numbers with space in between: ").strip().split()))
c = list(map(mult, b))
print("Sqaures:", c)

# 16
print("Output for (i) is 2")
print("Output for (ii) is NameError: name 'f' is not defined")
