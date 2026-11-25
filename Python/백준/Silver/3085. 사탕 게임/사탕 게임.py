#3085 04/17
import sys
def check(b):
    max_cnt = 1
    for i in range(N):
        max_col = 1
        max_row = 1
        for j in range(1, N):
            if b[i][j] == b[i][j-1]:
                max_row += 1
                max_cnt = max(max_cnt, max_row)
            else:
                max_row = 1
                
            if b[j][i] == b[j-1][i]:
                max_col += 1
                max_cnt = max(max_cnt, max_col)
            else:
                max_col = 1
                
    return max_cnt
    
answer = 0
#sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
candy = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for y in range(N):
    for x in range(N):
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if candy[y][x] != candy[ny][nx]:
                    candy[y][x], candy[ny][nx] = candy[ny][nx], candy[y][x]
                    answer = max(answer, check(candy))
                    candy[y][x], candy[ny][nx] = candy[ny][nx], candy[y][x]
print(answer)