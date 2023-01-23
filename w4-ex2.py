x = eval(input())
key_ll = list(x.keys())
key_ll.sort()
sorted_by_key = {i: x[i] for i in key_ll}
print(sorted_by_key)

# {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}