#1327 Oct 25, 2025
import sys
from collections import deque
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
gole = sorted(nums)
cnt = 0

q = deque([(tuple(nums), cnt)])

visit = set()

while q:
    arr, cnt = q.popleft()
    if list(arr)== gole:
        print(cnt)
        break
    
    for i in range(N-K+1):
        new_list = list(arr)
        new_list[i:i+K] = reversed(new_list[i:i+K])
        new_tuple = tuple(new_list)
        
        if new_tuple not in visit:
            visit.add(new_tuple)
            q.append((new_tuple, cnt + 1))
else:
    print(-1)
        