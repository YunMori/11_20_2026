n = int(input())
w = list(list(map(int, input().split()))for _ in range(n))

visited = [False]*n

min_sum = 10000001

def dfs(start, now, depth, current_sum):
    global min_sum
    if depth == n:
        if w[now][start] != 0:
            current_sum += w[now][start]
            min_sum = min(min_sum, current_sum)
        return

    if current_sum > min_sum:
        return

    for j in range(n):
        if not visited[j] and w[now][j] != 0:
            visited[j] = True
            dfs(start, j, depth + 1, current_sum + w[now][j])
            visited[j] = False

for i in range(n):
    visited[i] = True
    dfs(i, i, 1, 0)
    visited[i] = False

print(min_sum)