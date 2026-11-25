N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in range(len(A)):
    if A[i]<X:
        B.append(A[i])
C = ' '.join([str(_) for _ in B])
print(C)