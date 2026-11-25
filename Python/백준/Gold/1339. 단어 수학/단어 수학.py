#1339 05/07
import sys
from collections import defaultdict
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
s = list(list(map(str, sys.stdin.readline().strip())) for _ in range(N))
weight = defaultdict(int)

for word in s:
    p = len(word)-1
    for ch in word:
        weight[ch] += 10**p
        p -= 1

power = 9
x = sorted(weight.items(), key= lambda x : x[1], reverse=True)
for ch, _ in x:
    weight[ch] = power
    power -= 1

result = 0
for word in s:
    for ch in range(len(word)):
        word[ch] = weight[word[ch]]
    result += int(''.join(map(str, word)))
print(result)