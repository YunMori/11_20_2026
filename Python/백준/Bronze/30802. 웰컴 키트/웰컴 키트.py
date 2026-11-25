N = int(input())
T_list = list(map(int,input().split()))
T,P = map(int,input().split())
T_count = 0
for i in T_list:
    if i <= T and i != 0:
        T_count += 1
    elif i > T and i != 0:
        if i%T != 0:
            T_count += ((i//T)+1)
        else:
            T_count += ((i//T))
L, R = N//P, N%P

print(f'{T_count}')
print(f'{L} {R}')