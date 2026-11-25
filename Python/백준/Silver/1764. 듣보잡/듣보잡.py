#1764
from collections import deque
Dont_Listen, Dont_Look = map(int,input().split())
Dont_Listen_List, Dont_Look_List = deque(), deque()
for _ in range(Dont_Listen):
    Dont_Listen_List.append(input())
for _ in range(Dont_Look):
    Dont_Look_List.append(input())
result = list(set(Dont_Listen_List).intersection(set(Dont_Look_List)))
result.sort()
print(len(result))
for i in result:
    print(i)