x = list(input())
y = "".join(x)
summation = 0
for i in x:
    summation += int(i)**len(x)
if summation == int(y):
    print("yes")
else:
    print("no")
