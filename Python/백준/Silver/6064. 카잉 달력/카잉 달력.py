from math import lcm
T = int(input())
for _ in range(T):
    M, N, g_x, g_y = map(int, input().split())
    max_len = lcm(M, N)
    answer = -1

    for year in range(g_x, max_len + 1, M):

        if (year - 1) % N + 1 == g_y:
            answer = year
            break

    print(answer)