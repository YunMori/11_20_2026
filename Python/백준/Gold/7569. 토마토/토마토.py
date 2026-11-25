#7569 04/29
import sys
from collections import deque
def bfs():
    global N, M, H
    p_list_z = [-1, 1, 0, 0, 0, 0]
    p_list_y = [0, 0, -1, 1, 0, 0]
    p_list_x = [0, 0, 0, 0, -1, 1]
    q = deque()
    q.extend(result)
    cnt = -1
    while q:
        for _ in range(len(q)):
            z, y, x = q.popleft()
            for i in range(6):
                dz, dy, dx = z + p_list_z[i], y + p_list_y[i], x + p_list_x[i]
                if 0 <= dz < H and 0 <= dy < N and 0 <= dx < M:
                    if table[dz][dy][dx] == 0:
                        table[dz][dy][dx] = 1
                        q.append((dz, dy, dx))
        cnt += 1
    return cnt
        

# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
M, N, H = map(int, sys.stdin.readline().split())
table = []
for _ in range(H):
    r = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    table.append(r)
result = []
visit = [[[False]*M for _ in range(N)] for _ in range(H)]
for z in range(H):
    for y in range(N):
        for x in range(M):
            if table[z][y][x] == 1:
                result.append((z, y, x))
                visit[z][y][x] = True
            if table[z][y][x] == -1:
                visit[z][y][x] = True
check = False
re = bfs()
for z in range(H):
    for y in range(N):
        if table[z][y].count(0) > 0:
            check = True
if check:
    print(-1)
else:
    print(re)
