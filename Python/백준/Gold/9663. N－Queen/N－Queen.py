#9663 05/02
def checker(row, col):
    for r in range(row):
        c = Queen[r]
        if c == col or abs(r-row) == abs(c-col):
            return False
    return True

def counter(row, N):
    if row == N:
        return 1
    cnt = 0
    for col in range(N):
        if checker(row, col):
            Queen[row] = col
            cnt += counter(row+1, N)
    return cnt

N = int(input())
Queen = [-1]*N
print(counter(0, N))