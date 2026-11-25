T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    dp = [a for a in range(n+1)]
    for j in range(k):
        for x in range(1, n+1):
            dp[x] = dp[x] + dp[x-1]


    print(dp[-1])
