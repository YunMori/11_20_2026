#11047 05/03
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0
while True:
    if K == 0:
        break
    arr_v = [0]*N
    for i in range(N):
        arr_v[i] = K//arr[i]
        if arr_v[i] == 0:
            arr_v[i] = 100000001
    a = arr_v.index(min(arr_v))
    K = K - (arr[a]*min(arr_v))
    cnt += min(arr_v)
print(cnt)