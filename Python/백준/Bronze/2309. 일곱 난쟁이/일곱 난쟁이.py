#2309 04/17
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
max_height = 100
height = [int(sys.stdin.readline()) for _ in range(9)]
total_height = sum(height)
for i in range(9):
    for j in range(9):
        total_height = sum(height)
        if i != j:
            total_height -= (height[i]+height[j])
        if total_height == max_height:
            height[i], height[j] = 0, 0
            break
    if total_height == max_height:
        break
height.sort()
for i in height:
    if i != 0:
        print(i)