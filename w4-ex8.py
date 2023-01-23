x = input()
y = [print("yes") if x[:len(x)//2] == x[(len(x)+1)//2::] else print("no")]
