#2206 05/10
def bfs():
    Q =deque()
    Q.append((0, 0, 0))
    visit[0][0][0] = True
    cnt = 1
    while Q:
        # print(Q)
        for _ in range(len(Q)):
            x, y, state = Q.popleft()
            if x == M-1 and y == N-1:
                return cnt
            for i in range(4):
                dx, dy = x + p_list_x[i], y + p_list_y[i]
                if 0 <= dx < M and 0 <= dy < N:
                    # 이전것이 벽을 깨지 않았을때
                    if state == 0:
                        # 다음것이 0일때
                        if map_list[dy][dx] == 0 and not visit[dy][dx][state]:
                            Q.append((dx, dy, state))
                            visit[dy][dx][state] = True
                        # 다음것이 1일때
                        elif map_list[dy][dx] == 1 and not visit[dy][dx][state]:
                            c = 1
                            Q.append((dx, dy, c))
                            visit[dy][dx][1] = True
                    # 이 전것이 벽을 깼을때
                    elif state == 1:
                        #다음것이 0일때
                        if map_list[dy][dx] == 0 and not visit[dy][dx][state]:
                            Q.append((dx, dy, state))
                            visit[dy][dx][state] = True
        cnt += 1
    return -1
                    
import sys
from collections import deque
# from pprint import pprint
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N, M = map(int, sys.stdin.readline().split())
map_list = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    c = ' '.join(s)
    map_list.append(list(map(int, c.split())))
    
p_list_x = [1, -1, 0, 0]
p_list_y = [0, 0, 1, -1]
visit = [[[False, False] for _ in range(M)] for _ in range(N)]
print(bfs())
