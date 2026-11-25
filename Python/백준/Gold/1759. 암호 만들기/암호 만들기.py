from itertools import combinations

L, C = map(int, input().split())
board = sorted(list(map(str, input().split())))
con = 'bcdfghjklmnpqrstvwxz'
vow = 'aeiou'

for com in combinations(board, L):
    a = ''.join(com)
    c, v = 0, 0
    for i in a:
        if i in con:
            c += 1
        elif i in vow:
            v += 1
    if c >= 2 and v >= 1:
        print(a)