# 2579
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
step = [0]
for _ in range(N):
    step.append(int(sys.stdin.readline()))
if N == 1:
    print(step[1])
elif N == 2:
    print(step[1]+step[2])
else:
    dp = [0]*(N+1)
    dp[1] = step[1]
    dp[2] = step[2]+step[1]
    dp[3] = max(step[1]+step[3], step[2]+step[3])
    for i in range(4, N+1):
        dp[i] = max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])
    print(dp[N])
    