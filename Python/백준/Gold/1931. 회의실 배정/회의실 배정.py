#1931 05/02
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
result = 0
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

table.sort(key= lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
# print(table)
for i in range(N):
    start, end = table[i][0], table[i][1]
    if end_time <= start:
        end_time = end
        cnt += 1
print(cnt)
