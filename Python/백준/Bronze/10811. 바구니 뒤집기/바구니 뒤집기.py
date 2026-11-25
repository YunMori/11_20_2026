N, M  = map(int,input().split())
A = list(range(1,N+1))
for _ in range(M):
    i, j = map(int, input().split())
    a = A[i-1:j]
    a.reverse()
    A[i-1:j] = a
print(" ".join(map(str,A)))