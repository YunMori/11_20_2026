#1697
from collections import deque
def BFS(N, K, visit):
    visit[N] = True
    Q = deque([N])
    cnt = 0
    while Q:
        if visit[K]:
            return cnt
        for _ in range(len(Q)):# 경우의 수를 같은 cnt 레벨에서 처리
            x = Q.popleft()
            for i in [x+1, x-1, x*2]:
                if 0 <= i < 100001 and not visit[i]:
                    visit[i] = True
                    Q.append(i)
        cnt+=1
    return cnt

N, K = map(int, input().split())
visit = [False]*100001
print(BFS(N, K, visit))
