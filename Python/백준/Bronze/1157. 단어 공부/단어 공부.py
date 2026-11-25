A = input().lower()
B = []
for i in range(97,123):
    D = chr(i)
    B.append(A.count(D))
C = max(B)
if B.count(C) >= 2:
    print('?')
else:
    Br = B.index(C)

    print(chr(Br+97).upper())