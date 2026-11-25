#10817 Oct 26, 2025
import sys
from bisect import bisect_left, bisect_right
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
answer = []
for i in m_list:
    answer.append(bisect_right(n_list, i)-bisect_left(n_list, i))
print(' '.join(map(str, answer)))
