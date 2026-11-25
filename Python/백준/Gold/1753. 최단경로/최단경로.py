#1753 05/13     
import sys, heapq
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
table = [[]for _ in range(V+1)]
cost = [1000000000]*(V+1)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    table[u].append((v, w))
cost[K] = 0
z = []
heapq.heappush(z, (0, K))
while z:
    c, n = heapq.heappop(z)
    for n_n, n_c in table[n]:
        if cost[n_n] > c + n_c:
            cost[n_n] = c + n_c
            heapq.heappush(z, (c + n_c, n_n))
for i in range(1, V+1):
    if cost[i] == 1000000000:
        print('INF')
    else:
        print(cost[i])