#11055 04/06
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = A[:]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+A[i])
print(max(dp))