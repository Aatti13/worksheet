x = eval(input())
sol = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        sol[i][j] = x[j][i]
print(sol)
