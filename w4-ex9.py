x = list(input())
y = int(input())
if y > len(x):
    print("Invalid")
else:
    del x[y-1]
    z = "".join(x)
    print(z)

