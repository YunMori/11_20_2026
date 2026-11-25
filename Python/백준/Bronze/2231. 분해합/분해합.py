#2231
N = int(input())
M = 0
while N != 1 and M < 1000000:
    M+=1
    M_1 = list(map(int,str(M)))
    M_2 = M+sum(M_1)
    if M_2 == N:
        break
if M == 1000000:
    M = 0
print(M)