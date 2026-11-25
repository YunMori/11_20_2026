N = int(input())
dp = [0, 1]
for i in range(1, N):
    dp.append(dp[i-1] + dp[i])
print(dp[N])