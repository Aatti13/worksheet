x = list(map(str, input().split(" ")))
ll = []
for _ in x:
    if len(_) % 2 == 0:
        ll.append(_)
print(ll)
