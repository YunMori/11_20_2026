from itertools import permutations
n = int(input())

for i in permutations([j for j in range(1, n+1)], n):
    print(*i)