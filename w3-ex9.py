x = eval(input())
y = eval(input())
sol = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for _ in range(len(x)):
    for i in range(len(x[0])):
        sol[_][i] = x[_][i]-y[_][i]
print(sol)