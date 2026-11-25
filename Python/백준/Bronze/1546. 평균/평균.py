B = list()
N = int(input())

A = list(map(int, input().split()))
M = max(A)
for i in range(N):
    B.append(A[i]/M*100)
E = sum(B)/len(B)
print(E)