#9613 04/21
import sys, math
from itertools import combinations
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    Nums = list(map(int, sys.stdin.readline().split()))
    comb_list = list(combinations(Nums[1:], 2))
    answer = 0
    for A, B in comb_list:
        answer += math.gcd(A, B)
    print(answer)