N, M = map(int, input().split())
table = list(map(int, input().split()))
start, end = 1, max(table)
result = 0
while start <= end:
    total = 0
    mid = (start + end)//2
    for i in table:
        if mid < i:
            total += (i-mid)
    if total < M:
        end  = mid -1
    else:
        result = mid
        start = mid + 1

print(result)