#BOJ_1003 05/18 분 초
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [[1, 0], [0, 1]]
    if N >= 2:
        for i in range(1, N+1):
            a = dp[i-1][0]+dp[i][0]
            b = dp[i-1][1]+dp[i][1]
            dp.append([a, b])
        print(dp[N][0], dp[N][1])
    else:
        print(dp[N][0], dp[N][1])