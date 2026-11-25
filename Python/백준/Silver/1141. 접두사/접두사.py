#1141 Oct 25, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt', 'rt')
N = int(sys.stdin.readline())
words = sorted(list(sys.stdin.readline().strip() for _ in range(N)), key= lambda x: -len(x))
answer = 0
for i in range(N):
    check = False
    for j in range(i):
        if words[j].startswith(words[i]):
            check = True
            break
    if not check:
        answer += 1
print(answer)