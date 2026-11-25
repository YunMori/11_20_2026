# 1012 하는중
import sys
from collections import deque, Counter

def BFS(table,a,b,N,M):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Q = [(a,b)]
    while Q:
        x, y = Q.pop(0)
        table[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if table[ny][nx] == 1:
                Q.append((nx, ny))
                table[ny][nx] = 0
                
        
    
T = int(input())

for _ in range(T):
    M, N, K = map(int,input().split())
    table = []
    for _ in range(N):
        table.append([0]*M)
    cnt = 0
    for _ in range(K):
        x, y = map(int,input().split())
        table[y][x] = 1
    for a in range(M):
        for b in range(N):
            if table[b][a] == 1:
                BFS(table,a,b,N,M)
                cnt += 1
    print(cnt)
    
        