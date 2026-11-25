#10828

import sys

def pop(stack) :
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop(-1)
    return stack

def size(stack):
    print(len(stack))
    
def empty(stack) :
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack) :
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

stack = []
N = int(sys.stdin.readline())
for _ in range(N):
    # S = list(map(str,input().split()))
    S = list(map(str,sys.stdin.readline().split()))
    if S[0] == 'push':
        stack.append(int(S[1]))
        continue
    
    elif S[0] == 'pop':
        pop(stack)
        continue
    
    elif S[0] == 'size':
        size(stack)
        continue
    
    elif S[0] == 'empty':
        empty(stack)
        continue
    
    elif S[0] == 'top':
        top(stack)
        continue
    
    