T = int(input())
for _ in range(T):
    A = []
    R, S = input().split()
    for i in range(len(S)):
        A.append(S[i]*int(R))
    print(''.join(map(str,A)))