from re import compile

rr = compile('\d{10}')
with open("sn1.txt", "r") as f:
    for line in f:
        print(rr.findall(line))

