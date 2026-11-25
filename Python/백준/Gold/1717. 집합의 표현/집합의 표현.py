#1717 05/10
#새로운 알고리즘 유니온 파인드
def find(x):
    if table[x] != x:
        table[x] = find(table[x])
    return table[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        table[b_root] = a_root

import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
table = [i for i in range(n+1)]

for p, a, b in arr:
    
    if p == 0:
        union(a, b)
        
    if p == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')