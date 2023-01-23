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
