#07/21
import sys

# sys.stdin = open('/Users/yunjongseo/Downloads/Sample_input.txt', 'rt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
answer = 0
A.sort(reverse=True)
for i in A:
    v = min(B)
    B.remove(v)
    answer += i*v
print(answer)