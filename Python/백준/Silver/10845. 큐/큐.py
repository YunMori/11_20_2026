#10845
from collections import deque
import sys
def solution(L, M):
    if M[0] == 'push':
        L.append(M[1])
    elif M[0] == 'pop':
        if len(L) == 0:
            print(-1)
        else:
            print(L.popleft())
    elif M[0] == 'size':
        print(len(L))
    elif M[0] == 'empty':
        if L:
            print(0)
        else:
            print(1)
    elif M[0] == 'front':
        if L:
            print(L[0])
        else:
            print(-1)
    elif M[0] == 'back':
        if L:
            print(L[-1])
        else:
            print(-1)
    return
N = int(sys.stdin.readline())
L = deque()
for _ in range(N):
    M = deque(map(str, sys.stdin.readline().split()))
    solution(L, M)
    
    
