#10844 04/10
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
for i in range(1,10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if 0<=j-1<10 and 0<=j+1<10:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j ==  9:
                dp[i][j] = dp[i-1][j-1]
                
print(sum(dp[N])%1000000000)