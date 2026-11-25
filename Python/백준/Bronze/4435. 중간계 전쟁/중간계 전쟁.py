T = int(input())
GG = [1,2,3,3,4,10]
SS = [1,2,2,2,3,5,10]
for a in range(T):
    NG = 0
    NS = 0
    G = list(map(int,input().split()))
    S = list(map(int,input().split()))
    for g in range(len(G)):
        NG += G[g]*GG[g]
    for s in range(len(S)):
        NS += S[s]*SS[s]
    a=a+1
    if NG > NS :
        print('Battle %d: Good triumphs over Evil'%a)
    elif NG < NS:
        print('Battle %d: Evil eradicates all trace of Good'%a)
    elif NG==NS:
        print('Battle %d: No victor on this battle field'%a)