#9275 04/29
import sys
from collections import defaultdict
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    table = defaultdict(int)
    for _ in range(n):
        name, type = sys.stdin.readline().split()
        table[type] += 1
    result = 1
    for i in table.values():
        result *= (i+1)
    print(result-1)