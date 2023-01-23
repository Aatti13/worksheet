from re import compile
from collections import Counter as cc

r1, r2 = compile('\w'), compile('\w+')
ll1, ll2 = [], []

with open("sn1.txt", "r") as f:
    for line in f:
        for _ in r1.findall(line):
            ll1.append(_)
        for i in r2.findall(line):
            ll2.append(i)

print(f"Char Freq: {dict(cc(ll1))}\nWord Freq: {dict(cc(ll2))}")
