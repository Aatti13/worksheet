x = eval(input())
one = int(input("Enter element: "))
other = int(input("Enter other element: "))
x[one-1], x[other-1] = x[other-1], x[one-1]
print(x)