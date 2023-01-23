from re import compile

x = input()
r1 = compile(f'{x}')

with open("sn1.txt", "r") as f:
    for line in f:
        print(r1.findall(line))
