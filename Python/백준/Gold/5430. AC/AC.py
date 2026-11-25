#5430 04/28
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    p = list(map(str, sys.stdin.readline().strip()))
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    if n == 0:
        Q = deque()
    else:
        Q = deque(map(int, arr[1:-1].split(',')))
    reverse = False
    error = False
    for i in p:
        if i == 'R':
            reverse = not reverse
        if i == 'D':
            if len(Q) <= 0:
                error = True
                break
            if reverse:
                Q.pop()
            else:
                Q.popleft()
    if error:
        print('error')
    else:
        if reverse:
            Q.reverse()
            print('[' + ','.join(map(str,Q)) + ']')
        else:
            print('[' + ','.join(map(str,Q)) + ']')
        
    