N,M = map(int,input().split())
A = [input().split()for _ in range(N)]
B = [input().split()for _ in range(N)]
C = []
for a in range(N):
    for i in range(M):
        C.append(int(A[a][i])+int(B[a][i]))
print(' '.join(map(str, C)))