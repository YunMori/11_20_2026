import sys

def solve():
    n = int(sys.stdin.readline().strip())
    

    is_imyeon = False
    if n == 4 or n >= 6:
        digit_sum = sum(int(d) for d in str(n))
        if digit_sum % 2 == 1:
            is_imyeon = True
            

    is_imhyun = False
    if n == 2 or n == 4:
        is_imhyun = True
    elif n > 1:

        temp = n
        factors = set()
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors.add(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
            
        is_prime = (len(factors) == 1 and n in factors)

        if not is_prime and len(factors) % 2 == 0:
            is_imhyun = True

    # 3. 결과 출력
    if is_imyeon and is_imhyun:
        print(4)
    elif is_imyeon:
        print(1)
    elif is_imhyun:
        print(2)
    else:
        print(3)
solve()