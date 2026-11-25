#1005 05/09

def dfs(W):
    if dp[W] != -1:
        return dp[W]
    max_time = 0
    for i in table[W]:
        max_time = max(max_time,dfs(i))
    dp[W] = max_time + rules[W]
    return dp[W]
    
import sys
sys.setrecursionlimit(5000)
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    table = {i : [] for i in range(1, N+1)}
    rules = [0] + list(map(int, sys.stdin.readline().split()))
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        table[y].append(x)
    W = int(sys.stdin.readline())
    dp = [-1]*(N+1)
    print(dfs(W))
    