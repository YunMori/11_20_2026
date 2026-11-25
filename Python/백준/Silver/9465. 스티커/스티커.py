#9465
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input.txt','rt')
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    table = list((list(map(int, sys.stdin.readline().split()))) for _ in range(2))
    dp = [[-1]*N for _ in range(2)]
    dp[0][0] = table[0][0]
    dp[1][0] = table[1][0]
    if N == 1:
        print(max(dp[0][0],dp[1][0]))
        continue
    dp[0][1] = dp[1][0]+table[0][1]
    dp[1][1] = dp[0][0]+table[1][1]
    for i in range(2,N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2])+table[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2])+table[1][i]
    print(max(dp[0][-1], dp[1][-1]))