import heapq

N = int(input())
left = []
right = []
result = []

for _ in range(N):
    x = int(input())
    if x != 0:
        if x > 0:
            heapq.heappush(right, x)
        else:
            heapq.heappush(left, -x)
    else:
        if not left and not right:
            result.append('0')
        elif not left:
            result.append(str(heapq.heappop(right)))
        elif not right:
            result.append(str(-heapq.heappop(left)))
        else:
            if left[0] <= right[0]:
                result.append(str(-heapq.heappop(left)))
            else:
                result.append(str(heapq.heappop(right)))

print('\n'.join(result))