#1049 Oct 19, 2025
import sys
import math

# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt', 'rt')

#N = 끊어진 기타줄 갯수
#M = 기타줄 브랜드 갯수
N, M = map(int, sys.stdin.readline().split())

min_a = 1001
min_b = 1001
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    min_a = min(a, min_a)
    min_b = min(b, min_b)

op_1 = min_a * math.ceil(N/6)
op_2 = min_b*N
op_3 = min_a * (N//6) + min_b*(N%6)
print(min(op_1, op_2, op_3))