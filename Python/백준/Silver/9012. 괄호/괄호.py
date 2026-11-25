#9012
T = int(input())
for _ in range(T):
    N = input()
    i, j = 0, 0
    for z in N:
        if i-j < 0:
            break
        if z == '(':
            i += 1
        else:
            j += 1
    if i != j:
        print('NO')
        continue
    else:
        print('YES')