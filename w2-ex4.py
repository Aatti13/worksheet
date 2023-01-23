x = list(input())
y = "".join(x)
summation, prod = 0, 1
for i in x:
    summation += int(i)
    prod *= int(i)
total = summation + prod
if total == int(y):
    print("yes")
else:
    print("no")
    