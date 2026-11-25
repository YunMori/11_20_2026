from itertools import permutations
N, M = map(int,input().split())
N_list = list(map(int, input().split()))
answer = 0
for i in permutations(N_list,3):
    if sum(i) > answer and sum(i) <= M:
        answer = sum(i)
print(answer)