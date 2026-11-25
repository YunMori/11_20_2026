N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = 0
for i in range(N):
    if A[i]<=B[i]:
        Q+=1

print(Q)