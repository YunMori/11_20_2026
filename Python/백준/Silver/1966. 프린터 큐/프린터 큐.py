#1966 Nov 1, 2025
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (3).txt','rt')

T = int(sys.stdin.readline())
for _ in range(T):
    N, target = map(int, sys.stdin.readline().split())
    Q = deque(map(int, sys.stdin.readline().split()))
    important_check = deque(sorted(Q, reverse= True))
    cnt = 0
    while Q:
        # print(Q)
        # print(important_check,'aaaa')
        # print(target, 'tttttt')
        if Q[0] == important_check[0]:
            N -= 1
            cnt+=1
            Q.popleft()
            important_check.popleft()
            if target == 0:
                break
            else:
                target -= 1
        else:
            Q.rotate(-1)
            if target == 0:
                target = N-1
            else:
                target -= 1
                
    print(cnt)
