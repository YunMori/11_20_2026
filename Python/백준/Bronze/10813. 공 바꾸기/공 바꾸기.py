N, M = map(int, input().split())
A = list(range(1, N+1))
for _ in range(M):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    A[a], A[b] = A[b], A[a]
print(" ".join(map(str,A)))