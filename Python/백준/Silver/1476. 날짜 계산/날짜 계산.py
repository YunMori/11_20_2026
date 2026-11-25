#1476 04/17
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
E, S, M = 0, 0, 0
a, b, c = map(int, sys.stdin.readline().split())
cnt = 1
while True:
    E += 1
    if E > 15:
        E = 1
    S += 1
    if S >28:
        S = 1
    M += 1
    if M >19:
        M = 1
    if E == a and S == b and M == c:
        break
    cnt += 1
print(cnt)