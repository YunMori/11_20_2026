#10815 Nov 1, 2025
import sys
from bisect import bisect_left, bisect_right
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (3).txt','rt')

N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
mums = list(map(int, sys.stdin.readline().split()))

answer = list()
for i in mums:
    l = bisect_left(nums, i)
    r = bisect_right(nums, i)
    cnt = r-l
    answer.append(cnt)
print(' '.join(map(str, answer)))
