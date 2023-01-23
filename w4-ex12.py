def replace(n, k, m):
    if k in n:
        n[n.index(k)] = m
        # del n[n.index(k)]
        y = "".join(n)
    else:
        y = "Invalid"
    return y


x = list(input())
rep = input()
new = input()
print(replace(x, rep, new))