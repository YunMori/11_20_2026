#1080 Oct 22, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt', 'rt')

def flip(matrix, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = 1 - matrix[i][j]
            
            
N, M = map(int, sys.stdin.readline().split())
A = list(list(map(int, sys.stdin.readline().strip())) for _ in range(N))
B = list(list(map(int, sys.stdin.readline().strip())) for _ in range(N))
cnt = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(A, i, j)
            cnt += 1
if A == B:
    print(cnt)
else:
    print(-1)