x = list(map(int, input().split(" ")))
p = 1
for i in x:
    p *= i
print(p/100)