#1260
from collections import deque
import sys
def DFS(table, V, visit):
    visit.append(V)
    for i in table:
        if V in i:
            for j in i:
                if j not in visit:
                    DFS(table, j, visit)
    return visit

def BFS(table, V, visit):
    Q = deque()
    Q.append(V)
    visit.append(V)
    while Q:
        x = Q.popleft()
        for i in table:
            if x in i:
                for j in i:
                    if j not in visit:
                        Q.append(j)
                        visit.append(j)
    return visit

# sys.stdin = open('/Users/yunjongseo/Downloads/input.txt', 'rt')
N, M, V = map(int, sys.stdin.readline().split())
table = []
for _ in range(M):
    table.append(list(map(int, sys.stdin.readline().split())))
for i in table:
    i.sort()
table.sort()
    
# print(table)
print(' '.join(map(str, DFS(table, V, visit = []))))
print(' '.join(map(str, BFS(table, V ,visit = []))))
