#BOJ_2302 05/21 분 초
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/output (1).txt', 'rt')
N = int(sys.stdin.readline())
dp = [0]*41
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]
M = int(sys.stdin.readline())
start = 1
answer = 1
for _ in range(M):
    x = int(sys.stdin.readline())
    l = x-start
    answer *= dp[l]
    start = x+1
answer *= dp[N-(start-1)]
print(answer)