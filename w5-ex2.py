from re import compile

r1 = compile('["A-Z"]["a-z"]+ \d{2}')
with open("sn1.txt", "r") as f:
    for line in f:
        print(r1.findall(line))
