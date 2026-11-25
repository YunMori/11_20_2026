#11052 04/14
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
P = [0]+list(map(int, sys.stdin.readline().split()))
dp = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i],dp[i-j]+P[j])
print(dp[N])
