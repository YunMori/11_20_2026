k = int(input())
board = input().split()

visited = [False]*10

answer = []

def check(a, b, op):
    if op == '<':
        return a < b
    if op == '>':
        return a > b
    return False

def dfs(depth, nums):
    if depth == k+1:
        answer.append(nums)
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(int(nums[-1]), i, board[depth-1]):
                visited[i] = True
                dfs(depth + 1, nums + str(i))
                visited[i] = False
dfs(0, '')
print(answer[-1])
print(answer[0])

