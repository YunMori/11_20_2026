n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
arr = arr + [[arr[0][0], arr[0][1]]]
a, b = 0, 0
for i in range(n):
    a = a + arr[i][0]*arr[i+1][1]
    b = b + arr[i+1][0]*arr[i][1]
answer = abs(a-b)/2
print(f'{answer:.1f}')