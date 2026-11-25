from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    a = list(combinations(arr, i))
    for i in range(len(a)):
        b = sum(a[i])
        if b == S:
            cnt +=1
print(cnt)