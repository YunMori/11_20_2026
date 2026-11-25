#1541 05/07
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
f = list(sys.stdin.readline().split('-'))
for i in range(len(f)):
    re = []
    if '+' in f[i]:
        re.extend(map(int, f[i].split('+')))
        f[i] = sum(re)
f = list(map(int, f))
answer = f[0]
for i in range(1, len(f)):
    answer -= f[i]
print(answer)