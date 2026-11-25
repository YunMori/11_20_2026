#1744 05/01
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input (10).txt', 'rt')
N = int(sys.stdin.readline())
arr_p = []
arr_z = []
arr_m = []
for _ in range(N):
    i = int(sys.stdin.readline())
    if i == 0:
        arr_z.append(i)
    elif i < 0:
        arr_m.append(i)
    elif i > 0:
        arr_p.append(i)
arr_m.sort()
arr_p.sort(reverse=True)
re_m = 0
re_p = 0

if len(arr_m)%2 == 0:
    for i in range(0, len(arr_m), 2):
        a, b = arr_m[i]*arr_m[i+1], arr_m[i]+arr_m[i+1]
        re_m += max(a, b)
else:
    for i in range(0, len(arr_m)-1, 2):
        a, b = arr_m[i]*arr_m[i+1], arr_m[i]+arr_m[i+1]
        re_m += max(a, b)
    if len(arr_z) > 0:
        re_m += 0
    else:
        re_m += arr_m[-1]
    

if len(arr_p)%2 == 0:
    for i in range(0, len(arr_p), 2):
        a, b = arr_p[i]*arr_p[i+1], arr_p[i]+arr_p[i+1]
        re_p += max(a, b)
else:
    for i in range(0, len(arr_p)-1, 2):
        a, b = arr_p[i]*arr_p[i+1], arr_p[i]+arr_p[i+1]
        re_p += max(a, b)
    re_p += arr_p[-1]

print(re_m + re_p)


