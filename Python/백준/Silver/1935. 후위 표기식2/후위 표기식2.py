#1935 04/19
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip())
num = list(int(sys.stdin.readline()) for _ in range(N))

num_dic = {chr(65+i): num[i] for i in range(N)}

stack = []
for i in range(len(arr)):
    if arr[i] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b+a)
    elif arr[i] == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif arr[i] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b*a)
    elif arr[i] == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    else:
        stack.append(num_dic[arr[i]])
print(f'{stack[0]:.2f}')