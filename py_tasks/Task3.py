# TASK 3

# 1
List = [1, 2, 3, 'a', 'xyz', 'abc123', 1 + 2j, 3.14, 0.01, 10.0]
print(List)


# 2
i = [10, 25, 31, 47, 56]
print(i[:2], "\n", i[-2:], "\n", i[1:4])


# 3
x = list(range(1, 6))
Sum, Prod = 0, 1
for i in x:
    Sum = Sum + i
    Prod = Prod * i
print("Sum is:", Sum, "\nProduct is:", Prod)


# 4
a = [75, 10, 29, 57, 99]
a.sort()
print("In list,\n", a, "\nlargest number is:", a[-1], "and smallest number is:", a[0])


# 5
a = list(range(16))
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(a)
print(b)


# 6
a = list(range(1, 31))
b = a[:5]
c = a[-5:]
d = []
b.extend(c)
for i in b:
    d.append(i*i)
print(b, d)


# 7
a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]
a[5:] = b
print(a)


# 8
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print(a)


# 9
i = int(input("Enter a natural number to get squares in dictionary format: "))
a = {x: x*x for x in range(1, i + 1)}
print(a)


# 10
print("Enter values in comma-separated and without space format: ")
i = input().split(',')
print(i)
j = (tuple(i))
print(j)
