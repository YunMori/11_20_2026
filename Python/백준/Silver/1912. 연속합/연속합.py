#1912 04/ 04
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
cur_sum, max_sum = 0, table[0]
for i in range(N):
    cur_sum = max(cur_sum+table[i], table[i])
    max_sum = max(cur_sum, max_sum)
print(max_sum)