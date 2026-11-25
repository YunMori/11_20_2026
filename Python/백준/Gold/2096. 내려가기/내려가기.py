#2096 05/10
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
dp_max = list(map(int, sys.stdin.readline().split()))
dp_min = dp_max[:]
for i in range(N-1):
    table = list(map(int, sys.stdin.readline().split()))
    c_max = [0, 0, 0]
    c_min = [0, 0, 0]
    for j in range(3):
        a, b, c = j-1, j, j+1
        if j == 0:
            v_max = max(dp_max[b], dp_max[c])
            v_min = min(dp_min[b], dp_min[c])
            c_max[j] = table[j] + v_max
            c_min[j] = table[j] + v_min
        elif j == 1:
            v_max = max(dp_max[a], dp_max[b], dp_max[c])
            v_min = min(dp_min[a], dp_min[b], dp_min[c])
            c_max[j] = table[j] + v_max
            c_min[j] = table[j] + v_min
        elif j == 2:
            v_max = max(dp_max[a], dp_max[b])
            v_min = min(dp_min[a], dp_min[b])
            c_max[j] = table[j] + v_max
            c_min[j] = table[j] + v_min

    dp_max = c_max
    dp_min = c_min
print(f'{max(dp_max)} {min(dp_min)}')