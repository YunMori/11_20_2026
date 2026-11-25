#1021 Oct 12, 2025

from collections import deque
import sys

# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')
    
N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
queue = deque(range(1, N + 1))
operations = 0

for target in targets:
    index = queue.index(target)
    if index <= len(queue) // 2:
        queue.rotate(-index)
        operations += index
        queue.popleft()
    else:
        queue.rotate(len(queue) - index)
        operations += len(queue) - index
        queue.popleft()

print(operations)
