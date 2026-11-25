#1105 Oct 23, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt', 'rt')

L, R = map(str, sys.stdin.readline().split())

if len(L)!=len(R):
    print(0)
else:
    cnt = 0
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8' and R[i] == '8':
                cnt +=1 
            continue
        else:
            break
    print(cnt)

