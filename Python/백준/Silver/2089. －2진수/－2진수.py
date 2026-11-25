#2089 04/22
N = int(input())
if N == 0:
    print(0)
else:
    result = []
    while N != 0:
        b = N%(-2)
        N = N//(-2)
        if b < 0:
            b += 2
            N += 1
        result.append(b)
    result.reverse()
    print(''.join(map(str,result)))