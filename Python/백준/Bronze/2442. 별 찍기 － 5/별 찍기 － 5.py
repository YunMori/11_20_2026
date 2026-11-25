N = int(input())
for i in range(1, N+1):
    star_n = 2*i-1
    space = N-i

    answer = ' '*space + '*'*star_n
    print(answer)