#1934 04/21
import sys, math
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    answer = math.lcm(B, A)
    print(answer)