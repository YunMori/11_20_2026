import sys
N = int(sys.stdin.readline())
B = []
for i in range(N):
    A = int(sys.stdin.readline())
    B.append(A)
Bt = sorted(B)
for i in range(len(Bt)):
    print(Bt[i])