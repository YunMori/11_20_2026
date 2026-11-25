#4883 04/15
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    table = [[0, 0, 0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[float('inf')]*3 for _ in range(N+1)]
    dp[1][1] = table[1][1]
    dp[1][2] = dp[1][1]+table[1][2]
    dp[2][0] = table[2][0]+dp[1][1]
    dp[2][1] = table[2][1]+ min(dp[2][0], dp[1][1], dp[1][2])
    dp[2][2] = table[2][2]+ min(dp[2][1],dp[1][1], dp[1][2])
    for i in range(3, N+1):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1])+table[i][0]
        dp[i][1] = min(dp[i][0], dp[i-1][0], dp[i-1][1], dp[i-1][2])+table[i][1]
        dp[i][2] = min(dp[i][1], dp[i-1][1], dp[i-1][2])+table[i][2]
    # print(dp)
    print(f'{cnt}. {dp[N][1]}')
    cnt += 1