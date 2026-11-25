#BOJ_1149 05/21 분 초
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/output (1).txt', 'rt')
N = int(sys.stdin.readline())
R, G, B = [], [], []
for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    R.append(r)
    G.append(g)
    B.append(b)
dp_R, dp_G, dp_B = [0]*N, [0]*N, [0]*N
dp_R[0], dp_G[0], dp_B[0] = R[0], G[0], B[0]
for i in range(1, N):
    dp_R[i] = min(dp_G[i-1], dp_B[i-1])+ R[i]
    dp_G[i] = min(dp_R[i-1], dp_B[i-1])+ G[i]
    dp_B[i] = min(dp_R[i-1], dp_G[i-1])+ B[i]
print(min(dp_R[N-1], dp_G[N-1], dp_B[N-1]))
    

