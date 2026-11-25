#2493 Nov 1, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (3).txt','rt')

N = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))

stack = list()
answer = list()

for i in range(N):
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    
    if stack:
        answer.append(stack[-1]+1)
    else:
        answer.append(0)
    
    stack.append(i)
    
print(' '.join(map(str, answer)))
    
