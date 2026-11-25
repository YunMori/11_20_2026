#2293 04/14
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
n,k = map(int, sys.stdin.readline().split())
value = list(int(sys.stdin.readline()) for _ in range(n))
value.sort()
value = [0]+ value
dp = [0]*(k+1)
dp[0] = 1
for i in range(1,n+1):
    for j in range(value[i], k+1):
        dp[j] = dp[j]+dp[j-value[i]]

print(dp[k])