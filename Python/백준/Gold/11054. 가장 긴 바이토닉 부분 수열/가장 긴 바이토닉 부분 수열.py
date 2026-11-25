import bisect

L = int(input())
a = list(map(int, input().split()))
dp_r = []
tail_r = [0]*L
for i in range(L):
    b = bisect.bisect_left(dp_r, a[i])
    if b is len(dp_r):
        dp_r.append(a[i])
    else:
        dp_r[b] = a[i]
    tail_r[i] = b+1

dp_l = []
tail_l = [0]*L
for i in range(L-1,-1,-1):
    b = bisect.bisect_left(dp_l, a[i])
    if b is len(dp_l):
        dp_l.append(a[i])
    else:
        dp_l[b] = a[i]
    tail_l[i] = b+1

answer = 0
for i in range(L):
    c = tail_l[i] + tail_r[i]
    if answer < c:
        answer = c
print(answer-1)