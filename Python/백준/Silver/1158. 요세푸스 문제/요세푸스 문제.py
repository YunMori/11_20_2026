#1158 04/18
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N, K = map(int, sys.stdin.readline().split())
N_list = deque(i for i in range(1, N+1))
result = []
for _ in range(N):
    N_list.rotate(-K+1)
    result.append(N_list.popleft())
print(f'<{', '.join(map(str, result))}>')
