#1074
from pprint import pprint
import sys
def Binary_serch(N, x, y):
    global cnt, r, c
    if x == c and y == r:
        print(cnt)
        return
    if not(x <= c < x+(2**N) and y <= r < y+(2**N)):
        cnt+= 2**(2*N)
        return
    half = 2**(N-1)
    Binary_serch(N-1, x, y)
    Binary_serch(N-1, x+half, y)
    Binary_serch(N-1, x, y+half)
    Binary_serch(N-1, x+half, y+half)
    return
N, r, c = map(int, sys.stdin.readline().split())
cnt = 0
x, y = 0, 0
Binary_serch(N, x, y)