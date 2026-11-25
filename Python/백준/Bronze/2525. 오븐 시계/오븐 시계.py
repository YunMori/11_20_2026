A,B = map(int,input().split())
C = int(input())
if B+C<60:
    print(A,B+C)
else :
    if C>60 :
        A = A+((B+C)//60)
        B = (B+C)%60
        if A>= 24:
            A = A-24
    elif C<60 :
     if C+B>=60:
            A = A+((B+C)//60)
            B = (B+C)%60
            if A >=24:
                A = A-24
     elif C+B<60:
            A=A
            B=B+C

    elif A>=24:
        A=24-A
    print(A,B)