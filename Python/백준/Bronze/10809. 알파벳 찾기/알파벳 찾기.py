S = input()
A = [-1]*26
for i in range(len(S)):
    N = ord(S[i])-ord('a')
    if A[N] == -1 :
         A[N] = i
print(' '.join(map(str,A)))
