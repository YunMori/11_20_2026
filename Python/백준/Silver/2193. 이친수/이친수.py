N = int(input())
dp = [0]*(91)
dp[1], dp[2], dp[3], dp[4] = 1, 1, 2, 3
if N > 4:
    for i in range(5, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N])
else:
    print(dp[N])