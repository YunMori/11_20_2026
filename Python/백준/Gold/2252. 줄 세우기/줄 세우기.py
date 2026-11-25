#2252 05/12
def topology_sort():
    result = []
    Q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
    while Q:
        x = Q.popleft()
        result.append(x)
        for i in table[x]:
            indegree[i] -=1
            if indegree[i] == 0:
                Q.append(i)
    return result

import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N, M = map(int, sys.stdin.readline().split())
table = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    table[A].append(B)
    indegree[B] += 1

answer = ' '.join(map(str, topology_sort()))
print(answer)
