#10799 04/18
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
S = list(sys.stdin.readline().strip())
p = 0
result = []
for i in S:
    if i == '(':
        p+=1
    elif i == ')':
        p -= 1
    result.append(p)
answer = []
for i in range(1, len(result)-1):
    if result[i] > result[i+1] and result[i+1] == result[i-1]:
        answer.append(result[i+1])
    elif result[i] > result[i+1]:
        answer.append(result[i-1] - result[i])
print(sum(answer))