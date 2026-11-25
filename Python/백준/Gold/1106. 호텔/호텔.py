c, n = map(int, input().split())
arr= [tuple(map(int, input().split())) for _ in range(n)]

dp = [float('inf')]*(c+100)
dp[0] = 0

for u, v in arr:
    for i in range(v, c+100):
    #     print(i)
    # print('~~~~~~~~~~~~~~~~~~~~')
        dp[i] = min(dp[i], dp[i-v]+u)
print(min(dp[c:]))