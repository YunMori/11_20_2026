#2563 05/13
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
max_val = 100*N
c = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
table = [[0]*100 for _ in range(101)]
cnt = 0
for x, y in c:
    for dy in range(10):
        for dx in range(10):
            nx, ny = x + dx, y + dy
            if table[ny][nx] != 1:
                table[ny][nx] = 1
                cnt += 1
print(cnt)
                
        