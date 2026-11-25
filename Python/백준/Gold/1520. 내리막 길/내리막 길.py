from functools import lru_cache


def main():
    M, N = map(int, input().split())
    grid = []
    for _ in range(M):
        grid.append(list(map(int, input().split())))

    memo = [[-1] * N for _ in range(M)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        if x == M - 1 and y == N - 1:
            return 1
        if memo[x][y] != -1:
            return memo[x][y]
        memo[x][y] = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] < grid[x][y]:
                memo[x][y] += dfs(nx, ny)
        return memo[x][y]

    stack = [(0, 0, False)]
    memo = [[-1] * N for _ in range(M)]

    while stack:
        x, y, processed = stack.pop()
        if x == M - 1 and y == N - 1:
            memo[x][y] = 1
            continue
        if processed:
            total = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] < grid[x][y]:
                    if memo[nx][ny] != -1:
                        total += memo[nx][ny]
            memo[x][y] = total
            continue
        if memo[x][y] != -1:
            continue
        stack.append((x, y, True))
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] < grid[x][y]:
                if memo[nx][ny] == -1:
                    stack.append((nx, ny, False))

    print(memo[0][0] if memo[0][0] != -1 else 0)


main()