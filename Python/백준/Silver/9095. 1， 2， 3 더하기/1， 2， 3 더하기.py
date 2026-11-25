#1260
L = {}
def what(x):
    global L
    if x in L:
        return L[x]
    if x == 1:
        L[1] = 1
        return 1
    elif x == 2:
        L[2] = 2
        return 2
    elif x == 3:
        L[3] = 4
        return 4
    elif x == 4:
        L[4] = 7
        return 7
    else:
        return what(x-1)+what(x-2)+what(x-3)

T = int(input())
for _ in range(T):
    x = int(input())
    result = what(x)
    print(result)