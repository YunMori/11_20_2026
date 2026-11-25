#1270 Oct 19, 2025

import sys
from collections import Counter

# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

n = int(sys.stdin.readline())

for _ in range(n):
    T = list(map(int, sys.stdin.readline().split()))
    N = T[0]//2
    Ti = T[1:] 
    I = Counter(Ti)
    for i, j in I.items():
        if j > N:
            print(i)
            break
    else:
        print('SYJKGW')
    