#BOJ_1010 05/18 분 초
import sys, math
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    table = list(map(int, sys.stdin.readline().split()))
    answer = math.comb(max(table), min(table))
    print(answer)