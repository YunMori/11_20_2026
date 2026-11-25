#1934 04/21
import sys, math
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
N = int(sys.stdin.readline())
s = str(math.factorial(N))
s = s[::-1]
cnt = 0
for i in range(len(s)):
    if s[i] == '0':
        cnt += 1
    else:
        break
print(cnt)
    