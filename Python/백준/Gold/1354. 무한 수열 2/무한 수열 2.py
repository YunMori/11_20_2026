#1354 Oct 25, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N, P, Q, X, Y = map(int, sys.stdin.readline().split())
A_dic = {0:1}

def serching(i):
    if i in A_dic:
        return A_dic[i]
    if (i//P)-X <= 0:
        A_dic[(i//P)-X] = 1
    if (i//Q)-Y <= 0:
        A_dic[(i//Q)-Y] = 1
    A_dic[i] = serching((i//P)-X) + serching((i//Q)-Y)
    return A_dic[i]
print(serching(N))