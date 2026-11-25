# 2468
import sys
from collections import deque
# from pprint import pprint
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
# print(N)
# print(grid)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_group = 0
for rain in range(101):
    # 비가 rain 만큼 왔을때 살아남는가?
    live = [[False]*N for _ in range(N)]
    # print(rain)
    for y in range(N):
        for x in range(N):
            if grid[y][x] <= rain:
                live[y][x] = True
    # pprint(live)
    cnt = 0
    for y in range(N):
        for x in range(N):
             if not live[y][x]:
                Q = deque([(x, y)])

                while Q:
                    xx, yy = Q.popleft()
                    for i in range(4):
                        nx, ny = xx + dx[i], yy + dy[i]

                        if 0 <= nx < N and 0 <= ny < N and not live[ny][nx]:
                            live[ny][nx] = True
                            Q.append((nx, ny))
                cnt +=1
    # print(cnt)

    if cnt == 0:
        break
    max_group = max(max_group, cnt)
# print("================")
print(max_group)
# print("================")
# pprint(grid)
# pprint(live)
                 