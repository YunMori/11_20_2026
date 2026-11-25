#1932
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input.txt', 'rt')
N = int(sys.stdin.readline())
table = list()
for _ in range(N):
    table.append(list(map(int,sys.stdin.readline().split())))
dp = [[-1]*(i+1)for i in range(N)]

dp[0][0] = table[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]+table[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1]+table[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+table[i][j]
print(max(dp[-1]))