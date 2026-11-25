#1235 Oct 15, 2025
import sys

# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N = int(sys.stdin.readline())
s_table = list(sys.stdin.readline().strip() for _ in range(N))
length  = len(s_table[0])

for i in range(1, length+1):
    seen = set()
    for num in s_table:
        seen.add(num[-i:])
    if len(seen) == N:
        print(i)
        break
