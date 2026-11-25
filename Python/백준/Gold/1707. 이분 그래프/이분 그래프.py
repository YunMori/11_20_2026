from collections import deque

k = int(input())
for _ in range(k):
    flag = False
    V, E = map(int, input().split())
    dic  = {i : [] for i in range(1, V+1)}
    visited = [0]*(V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        dic[u].append(v)
        dic[v].append(u)
    for i in range(1, V+1):
        if visited[i] == 0:
            visited[i] = 1
            q = deque([i])
            while q:
                z = q.popleft()
                for j in dic[z]:
                    if visited[j] == 0:
                        visited[j] = 3-visited[z]
                        q.append(j)
                    else:
                        if visited[j] == visited[z]:
                            flag = True
                            break
                if flag:
                    break
    if not flag:
        print('YES')
    else:
        print('NO')
