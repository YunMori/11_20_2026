from itertools import combinations
N, K = map(int, input().split())
print(len(list(map(str, combinations(range(N),K)))))