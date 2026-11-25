#1406 04/17
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
left = list(map(str, sys.stdin.readline().strip()))
right = deque()
M = int(sys.stdin.readline())
for _ in range(M):
    scon = list(map(str, sys.stdin.readline().split()))
    if scon[0] == 'P':
        left.append(scon[1])
    elif scon[0] == 'L':
        if len(left) == 0:
            continue
        else:
            right.appendleft(left.pop())
    elif scon[0] == 'D':
        if len(right) == 0:
            continue
        else:
            left.append(right.popleft())
    elif scon[0] == 'B':
        if len(left) == 0:
            continue
        else:
            left.pop()
    # print(scon[0], left+right)

print(''.join(left+list(right)))