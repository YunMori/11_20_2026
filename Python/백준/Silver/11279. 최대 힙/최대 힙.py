import heapq
import sys
n = int(sys.stdin.readline())
heap = []
results = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            results.append(str(-heapq.heappop(heap)))
        else:
            results.append('0')
    else:
        heapq.heappush(heap, -x)
print('\n'.join(results))