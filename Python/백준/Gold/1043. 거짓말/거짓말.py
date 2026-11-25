#1043 Oct 19, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N, M = map(int, sys.stdin.readline().split())

truth = list(map(int, sys.stdin.readline().split()))
truth_people = truth[1:]

graph = list(list() for _ in range(N+1))
parties = list()

for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    party = data[1:]
    parties.append(party)
    
    for i in range(len(party)):
        for j in range(i + 1, len(party)):
            graph[party[i]].append(party[j])
            graph[party[j]].append(party[i])

visit = [False]*(N+1)

def DFS(v):
    visit[v] = True
    for never in graph[v]:
        if not visit[never]:
            DFS(never)

for person in truth_people:
    DFS(person)
    
cnt = 0
for party in parties:
    if not any(visit[person] for person in party):
        cnt += 1
print(cnt)