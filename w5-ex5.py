from re import compile
from collections import Counter as cc
ll = []
key_ll, value_ll = [], []
r1 = compile('\d')
with open("sn1.txt", "r") as f:
    for line in f:
        for _ in r1.findall(line):
            ll.append(_)
y = dict(cc(ll))
print(y)
for key, value in y.items():
    key_ll.append(key)
    value_ll.append(value)
o = key_ll[value_ll.index(max(value_ll))]
p = key_ll[value_ll.index(min(value_ll))]
print(f"Max: {o}\nMin: {p}")
