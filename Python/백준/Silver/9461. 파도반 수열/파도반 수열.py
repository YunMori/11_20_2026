#BOJ_9461 05/19 분 초
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/output (1).txt')
T = int(sys.stdin.readline())
P = [0]*101
P[1], P[2], P[3], P[4], P[5], P[6], P[7], P[8], P[9], P[10] = 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
for _ in range(T):
    N = int(sys.stdin.readline())
    if N <= 10:
        print(P[N])
    else:
        for i in range(10, N+1):
            P[i] = P[i-1] + P[i-5]
        print(P[N])
