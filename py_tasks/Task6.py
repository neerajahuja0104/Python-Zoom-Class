# TASK 6

# 1
a1 = input("Enter a string: ")
a2 = [a3 for a3 in a1 if a3.isupper() == 1]
print(a2)


# 2
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
pairs = {a4: a5 for (a4, a5) in zip(students, subjects)}
print(pairs)


# 4
def rev(a8):
    strlen = len(a8)
    for a9 in range(strlen - 1, - 1, - 1):
        yield a8[a9]


a6 = input("Enter a string to reverse: ")
a10 = []
for lett in rev(a6):
    a10.append(lett)
a10 = ''.join(a10)
print(a10)


# 5
def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


r1 = operate(inc, 3)
r2 = operate(dec, 3)
print(r1, r2)
