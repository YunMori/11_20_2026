L = []
LL = []
for _ in range(7):
    N = int(input())
    if N%2==1:
        LL.append(N)
    else:
        L.append(N)
if len(LL) == 0:
    print(-1)
else:
    print(sum(LL))
    print(min(LL))