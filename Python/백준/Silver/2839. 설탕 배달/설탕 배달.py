N = int(input())

for ct_5 in range(N//5,-1,-1):
    ct_3 = (N-ct_5*5)//3
    if ct_5*5+ct_3*3==N:
        print(ct_3+ct_5)
        break
else:
    print(-1)