x = eval(input())
y = eval(input())
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for _ in range(len(x)):
    for i in range(len(y[0])):
        for j in range(len(y)):
            result[_][i] = x[_][j] * y[j][_]
print(result)
