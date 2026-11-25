#BOJ_11053 05/21 분 초
import sys, bisect
# sys.stdin = open('/Users/yunjongseo/Downloads/output (1).txt', 'rt')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = []
for i in range(N):
    x = bisect.bisect_left(stack, A[i])
    if x == len(stack):
        stack.append(A[i])
    else:
        stack[x] = A[i]
print(len(stack))