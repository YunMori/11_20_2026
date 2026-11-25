#1929 04/16
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
M, N = map(int, sys.stdin.readline().split())
dp = [0]+[_ for _ in range(1, 1000000+1)]
dp[1] = False
for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        if i ==j:
            continue
        else:
            if dp[j]:
                dp[j] = False
for i in range(M, N+1):
    if dp[i]:
        print(dp[i])