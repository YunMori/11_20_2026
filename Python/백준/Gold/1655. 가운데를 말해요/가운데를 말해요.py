import heapq

N = int(input())
lower = []
upper = []
result = []

for _ in range(N):
    num = int(input())

    if len(lower) == len(upper):
        heapq.heappush(lower, -num)
    else:
        heapq.heappush(upper, num)

    if upper and -lower[0] > upper[0]:
        lo = -heapq.heappop(lower)
        up = heapq.heappop(upper)
        heapq.heappush(lower, -up)
        heapq.heappush(upper, lo)

    result.append(str(-lower[0]))

print('\n'.join(result))