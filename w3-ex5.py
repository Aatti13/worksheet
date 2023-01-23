x = eval(input())
even_list = []
odd_list = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        even_list.append(x[i])
    else:
        odd_list.append(x[i])
print(even_list, odd_list, sep="\n")