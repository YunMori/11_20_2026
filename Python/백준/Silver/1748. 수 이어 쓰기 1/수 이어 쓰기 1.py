N = int(input())
len_n = len(str(N))
ans = 0
for i in range(len_n-1):
    ans += 9*(10**i)*(i+1)

find = N-10**(len_n-1)+1

ans += find*len_n
print(ans)