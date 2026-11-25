I = input()
Y = []
for i in range(len(I)):
    A = I[i-1]
    if A in 'ABC' :
        A = 3
    elif A in 'DEF':
        A = 4
    elif A in 'GHI' :
        A = 5
    elif A in 'JKL' :
        A = 6
    elif A in 'MNO':
        A = 7
    elif A in 'PQRS':
        A =8
    elif A in 'TUV':
        A =9
    elif A in 'WXYZ':
        A = 10
    Y.append(int(A))
print(sum(Y))