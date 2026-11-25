#2606
from collections import deque

def BFS (Conection_List, visit, Computer_Number):
    if Computer_Number == 0:
        return len(visit)-1
    for a in Conection_List:
        if a[0] in visit:
            visit.add(a[1])
        elif a[1] in visit:
            visit.add(a[0])
    BFS(Conection_List, visit, Computer_Number-1)
    return len(visit)-1
Computer_Number = int(input())
Network_Number = int(input())
Conection_List = deque()
visit = set()
visit.add(1)
for _ in range(Network_Number):
    Conection_List.append(list(map(int,input().split())))
result = BFS (Conection_List, visit, Computer_Number)
print(result)