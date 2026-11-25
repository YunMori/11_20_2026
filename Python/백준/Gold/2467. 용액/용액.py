n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1
min_sum = (2000000001, left, right)
while left < right:
    current_sum = arr[left] + arr[right]

    if abs(current_sum) < min_sum[0]:
        min_sum = (abs(current_sum), left, right)

    if current_sum > 0:
        right -= 1
    elif current_sum < 0:
        left += 1
    else:
        min_sum = (0, left, right)
        break

print(f'{arr[min_sum[1]]} {arr[min_sum[2]]}')