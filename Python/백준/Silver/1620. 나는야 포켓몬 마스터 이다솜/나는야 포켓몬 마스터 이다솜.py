#1620 04/30
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt','rt')
N, M = map(int, sys.stdin.readline().split())
table_name = {}
table_num = {}
for i in range(1, N+1):
    s = sys.stdin.readline().strip()
    table_num[i] = s
    table_name[s] = i
for _ in range(M):
    want = sys.stdin.readline().strip()
    if want.isdigit():
        print(table_num[int(want)])
    else:
        print(table_name[want])