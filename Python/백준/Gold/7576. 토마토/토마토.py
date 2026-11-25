#7576 05/13
def bfs():
    global cnt
    Q = deque()
    Q.extend(a)
    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            visit[y][x] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx] and tomato[ny][nx] == 0:
                    visit[ny][nx] = True
                    tomato[ny][nx] = 1
                    Q.append((nx, ny))
        cnt += 1
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[False]*M for _ in range(N)]
a = []
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            a.append((x, y))
cnt = -1
bfs()

check = False
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 0:
            check = True
if check:
    print(-1)
else:
    print(cnt)            
