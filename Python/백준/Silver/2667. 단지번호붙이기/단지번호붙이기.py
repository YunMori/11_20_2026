# 2667
import sys
from collections import deque
from pprint import pprint

def BFS(x, y, N):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    table[y][x] = 0
    cnt = 1
    Q = deque([[x, y]])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                if table[ny][nx] == 1:
                    Q.append([nx, ny])
                    table[ny][nx] = 0
                    cnt+=1
                    # print(nx, ny, cnt)
        
    return cnt

N = int(input())
table = []
result = []
for _ in range(N):
    table.append(list(map(int, input())))
for y in range(N):
    for x in range(N):
        if table[y][x] == 1:
            result.append(BFS(x, y, N))
result.sort()
# print(result)
print(len(result))
for i in result:
    print(i)