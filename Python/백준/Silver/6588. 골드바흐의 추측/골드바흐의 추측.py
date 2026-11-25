#6588 04/16
import math, sys
prime = [True]*1000001
prime[0], prime[1] = False, False
for i in range(2, int(math.sqrt(1000000)+1)):
    if prime[i]:
        for j in range(i, 1000001, i):
            if i == j:
                continue
            else:
                prime[j] = False
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    check = False
    for a in range(3, n//2+1, 2):
        b = n - a
        if prime[a] and prime[b]:
            print(f'{n} = {a} + {b}')
            check = True
            break
    if not check:
        print("Goldbach's conjecture is wrong.")
 