N = int(input())
if N % 2 == 1:
    print(0)
else:
    dp = [0] * (N + 1)
    dp[0] = 1
    if N >= 2:
        dp[2] = 3
    for i in range(4, N + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]
    print(dp[N])