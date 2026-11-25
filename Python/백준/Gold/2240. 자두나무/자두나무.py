#2240 04/11
import sys
# from pprint import pprint
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt','rt')
T, W = map(int, sys.stdin.readline().split())
tree = [0]*(T+1)
for i in range(1,T+1):
    tree[i] = int(sys.stdin.readline())
dp = [[0]*(W+1) for _ in range(T+1)]
cnt = 0
for i in range(1, T+1):
    if tree[i] == 1:
        cnt+=1
        dp[i][0] = cnt
    else:
        dp[i][0] = dp[i-1][0]
for t in range(1, T+1):
    for w in range(1, W+1):
        cor = 1 if w%2 == 0 else 2
        if cor == tree[t]:
            dp[t][w] = dp[t-1][w]+1
        else:
            dp[t][w] = max(dp[t-1][w-1]+1, dp[t-1][w])
    
# print(tree)
print(dp[T][W])