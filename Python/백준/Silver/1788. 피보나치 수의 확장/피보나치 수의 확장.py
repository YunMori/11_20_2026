#1788 04/15
n = int(input())
if n >1:
    F = [0]*(n+1)
    F[0], F[1] = 0, 1
    for i in range(2,n+1):
        F[i] = (F[i-1]+F[i-2])%1000000000
    print(1)
    print(F[n])
elif n == 0:
    print(0)
    print(0)
else:
    F = [0]*(abs(n)+1)
    F[0], F[1] = 0, 1
    for i in range(2,abs(n)+1):
        F[i] = (F[i-1]+F[i-2])%1000000000
    if abs(n)%2 == 0:
        print(-1)
    else:
        print(1)
    print(F[abs(n)])
        