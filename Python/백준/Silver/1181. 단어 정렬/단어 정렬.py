N = int(input())
W_list = []
for _ in range(N):
    W_list.append(input())
# 중복 제거
W_list = list(set(W_list))

# 정렬: 길이 우선 → 동일 길이일 경우 사전 순
W_list.sort(key=lambda x: (len(x), x))

for i in W_list:
    print(i)