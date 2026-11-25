#2178 05/02
def bfs(start_x, start_y, N, M):
    Q = deque()
    cnt = 1
    Q.append((start_x, start_y, cnt))
    visit[start_y][start_x] = True
    while Q:
        for _ in range(len(Q)):
            x, y, cnt = Q.popleft()
            
            if x == M-1 and y == N-1:
                return cnt
            
            for i in range(4):
                dx, dy = x + p_list_x[i], y + p_list_y[i]
                if 0 <= dx < M and 0 <= dy < N and table[dy][dx] == '1' and not visit[dy][dx]:
                    Q.append((dx, dy, cnt+1))
                    visit[dy][dx] = True
    return cnt
                
    
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N, M = map(int, sys.stdin.readline().split())
table = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
p_list_x = [0, 0, -1, 1]
p_list_y = [-1, 1, 0, 0]
visit = [[False]*M for _ in range(N)]
print(bfs(0, 0, N, M))