def fibonacci(n):
    counter = 0
    ll = []
    first = 0
    second = 1
    temp = 0
    baller = False

    while counter <= n:
        # print(first)
        ll.append(first)
        temp = first + second
        first = second
        second = temp
        counter += 1
    return ll[n-1]


x = int(input())
print(fibonacci(x))