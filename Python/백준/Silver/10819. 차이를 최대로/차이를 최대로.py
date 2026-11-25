from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

answer = 0
for arr in permutations(a, n):
    arr = list(arr)
    c = 0
    for i in range(n-1):
        c += abs(arr[i]-arr[i+1])
    answer = max(answer, c)

print(answer)
