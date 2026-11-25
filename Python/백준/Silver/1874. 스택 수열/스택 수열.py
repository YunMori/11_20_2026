#2309 05/13
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
stack = []
result = []
a = 0
check = False
for _ in range(N):
    x = int(sys.stdin.readline())
    while a < x:
        a += 1
        stack.append(a)
        result.append('+')
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        check = True
        break
    if check:
        break
if check:
    print('NO')
else:
    for i in result:
        print(i)
    