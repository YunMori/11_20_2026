#1916 04/29
import sys , heapq
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
table = {i:[] for i in range(1, N+1)}
for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    table[s].append((e, c))
visit = [float('inf')]*(N+1)
start, target = map(int, sys.stdin.readline().split())
visit[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    cost, p = heapq.heappop(q)
    if visit[p] < cost:
        continue
    for n_p, n_co in table[p]:
        if visit[n_p] > cost + n_co:
            visit[n_p] = cost + n_co
            heapq.heappush(q,(visit[n_p], n_p))
print(visit[target])