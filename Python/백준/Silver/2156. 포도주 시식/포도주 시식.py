#2156 04/11
import sys
#sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt','rt')
n = int(sys.stdin.readline())
table = [0]
for _ in range(n):
    table.append(int(sys.stdin.readline()))
if n == 1:
    print(table[1])
elif n == 2:
    print(table[1]+table[2])
else:
    dp = [0]*(n+1)
    dp[1] = table[1]
    dp[2] = table[1]+table[2]
    # dp[3] = max(table[1]+table[3], table[2]+table[3])
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+table[i-1]+table[i],dp[i-2]+table[i], dp[i-1])
        
    print(max(dp))