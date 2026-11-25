import sys
N = int(sys.stdin.readline())
T = [0]*10000
for _ in range(N):
    j = int(sys.stdin.readline())-1
    T[j] += 1
for i in range(len(T)):
    if T[i] != 0:
        for _ in range(T[i]):
            print(i+1)
    else: continue
# pprint(T)