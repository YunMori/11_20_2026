#2004 04/21
def count_k(n, k):
    result = 0
    temp = k
    while temp <= n:
        result += n//temp
        temp *= k
    return result

import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
A, B = map(int, sys.stdin.readline().split())

two = count_k(A, 2) - count_k(B, 2) - count_k(A-B, 2)
five = count_k(A, 5) - count_k(B, 5) - count_k(A-B, 5)

print(min(two, five))
