# 9x9 격자판을 입력받습니다.
grid = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

# 최댓값과 그 위치를 초기화합니다.
max_value = -1
max_row = -1
max_col = -1

# 격자판을 순회하면서 최댓값과 위치를 찾습니다.
for i in range(9):
    for j in range(9):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            max_row = i + 1
            max_col = j + 1

# 결과를 출력합니다.
print(max_value)
print(max_row, max_col)