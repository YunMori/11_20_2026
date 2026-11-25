#1269 Oct 18, 2025
import sys

# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

A_N, B_N = map(int,sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

m_A = A-B
m_B = B-A

print(len(m_A)+len(m_B))
