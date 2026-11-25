n = int(input())
arr = list(map(int,input().split()))
flag = False
for i in range(n-1, 0, -1):
    if arr[i-1] > arr[i]:
        for j in range(n-1, i-1, -1):
            if arr[i-1] > arr[j]:
                flag = True
                temp = arr[i-1]
                arr[i-1] = arr[j]
                arr[j] = temp
                arr[i:] = reversed(arr[i:])
                break
    if flag:
        break
if flag:
    print(*arr)
else:
    print(-1)
