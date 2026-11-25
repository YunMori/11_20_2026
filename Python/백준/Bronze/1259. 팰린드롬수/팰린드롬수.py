#1259
while True:
    N = int(input())
    if N == 0:
        break
    N_list = list(''.join(str(N)))
    if N_list == N_list[::-1]:
        print('yes')
    else:
        print('no')