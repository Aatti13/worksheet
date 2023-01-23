X = eval(input())
Y = eval(input())

Z = [x for _, x in sorted(zip(Y, X))]
print(Z)