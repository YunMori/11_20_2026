#1927
from queue import PriorityQueue
import sys
N = int(sys.stdin.readline())
x_list = PriorityQueue(maxsize=N)

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if x_list.empty() == True:
            print(0)
        else:
            print(x_list.get(0))
    else:
        x_list.put(x)