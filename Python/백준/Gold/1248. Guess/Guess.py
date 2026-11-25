n = int(input())
board = input()
S = [[-1]*n for _ in range(n)]
idx = 0
a = [0]*n
for y in range(n):
    for x in range(y, n):
        S[y][x] = board[idx]
        idx += 1
# print(S)

def check(i):
    z = 0
    for j in range(i, -1, -1):
        z += a[j]
        if S[j][i] == '+' and z <= 0: return False
        if S[j][i] == '-' and z >= 0: return False
        if S[j][i] == '0' and z != 0: return False

    return True


def solve(i):
    if i == n:
        return True

    if S[i][i] == '+':
        for j in range(1, 11):
            a[i] = j
            if check(i):
                if solve(i+1) : return True

    if S[i][i] == '-':
        for j in range(-10, 0):
            a[i] = j
            if check(i):
                if solve(i + 1): return True

    if S[i][i] == '0':
        a[i] = 0
        if check(i):
            if solve(i + 1): return True

    return  False

solve(0)
print(' '.join(map(str, a)))