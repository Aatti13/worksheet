mtk = lambda x: print(f"m to km: {x/1000}km")
ktm = lambda x: print(f"km to m: {x*1000}m")
ch = int(input())
if ch ==1:
    mtk(int(input()))
elif ch == 2:
    ktm(int(input()))
else:
    print("Invalid")