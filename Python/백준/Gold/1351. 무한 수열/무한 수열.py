#1351 Oct 25, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N, P, Q = map(int, sys.stdin.readline().split())
A_dic = {0:1}

def serching(a):
    if a in A_dic:
        return A_dic[a]
    A_dic[a] = serching(a//P) + serching(a//Q)
    return A_dic[a]

print(serching(N))
    