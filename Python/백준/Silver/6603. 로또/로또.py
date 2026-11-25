#6603 04/30
import sys
from itertools import combinations
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt','rt')
while True:
    r = list(map(int, sys.stdin.readline().split()))
    k = r[0]
    if k == 0:
        break
    S = r[1:k+1]
    result = list(combinations(S, 6))
    for i in result:
        print(' '.join(map(str, i)))
    print()
    