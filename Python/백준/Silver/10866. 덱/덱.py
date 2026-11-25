#10866 04/18
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
result = deque()
for _ in range(N):
    scon = list(sys.stdin.readline().split())
    if scon[0] == 'push_front':
        result.appendleft(scon[1])
    elif scon[0] == 'push_back':
        result.append(scon[1])
    elif scon[0] == 'pop_front':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif scon[0] == 'pop_back':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif scon[0] == 'size':
        print(len(result))
    elif scon[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif scon[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    elif scon[0] == 'back':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
        