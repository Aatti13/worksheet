f_to_c = lambda x: print((5*(x-32))/9)
c_to_f = lambda x: print(1.8*x+32)
ch = int(input())
if ch == 1:
    f_to_c(int(input()))
elif ch == 2:
    c_to_f(int(input()))
else:
    print("Invalid")
