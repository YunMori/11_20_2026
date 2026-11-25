A, B = map(str,input().split())
rA = A[::-1]
rB = B[::-1]
rA = int(rA)
rB = int(rB)
if rA>rB :
    print(rA)
else:
    print(rB)