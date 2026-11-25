#1715 05/07
import sys
import heapq
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
Num_list = []
for _ in range(N):
    heapq.heappush(Num_list, int(sys.stdin.readline()))
cnt = 0
for _ in range(N-1):
        if len(Num_list) >= 2:
            a, b = heapq.heappop(Num_list),heapq.heappop(Num_list)
            heapq.heappush(Num_list, a+b)
        cnt += (a+b)
print(cnt)