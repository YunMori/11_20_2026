N = int(input())
M = int(input())
M_l = []
min_cnt = abs(N-100)

if M > 0:
    M_l = list(map(str, input().split()))



for i in range(1000001):
    r = str(i)

    flag = True

    for c in r:
        if c in M_l:
            flag = False
            break

    if flag:
        n_c = len(r) + abs(i - N)
        min_cnt = min(min_cnt, n_c)
print(min_cnt)
