#1654 05/12
def check(mid):
    cnt = 0
    for i in len_list:
        cnt += i//mid
    return cnt >= N

def binary(start, end):
    re = 0
    while start <= end:
        mid = (start+end)//2
        if check(mid):
            re = mid
            start = mid + 1
        else:
            end = mid -1
    return re

import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
K, N = map(int, sys.stdin.readline().split())
len_list = [int(sys.stdin.readline()) for _ in range(K)]
print(binary(1, max(len_list)))