#1302 Oct 19, 2025

import sys
from collections import Counter

# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N = int(sys.stdin.readline())

books = list()
for _ in range(N):
    books.append(sys.stdin.readline().strip())
counter = Counter(sorted(books))

b = 0
answer = str()
for i, j in counter.items():
    if j > b:
        b = j
        answer = i
    
print(answer)