#1138 Oct 25, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt', 'rt')

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

ml= [0]*N

for i in range(N):
    cnt = M[i]
    for j in range(N):
        if cnt == 0 and ml[j] == 0:
            ml[j] = i+1
            break
        if ml[j] == 0:
            cnt -= 1
print(' '.join(map(str, ml)))
        