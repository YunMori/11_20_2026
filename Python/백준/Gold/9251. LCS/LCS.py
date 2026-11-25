#9251
# import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/input.txt','rt')
x = input()
y = input()
LCS = [[-1]*(len(x)+1) for _ in range(len(y)+1)]
for i in range(len(x)+1):
    LCS[0][i] = 0
for j in range(len(y)+1):
    LCS[j][0] = 0
for i in range(1, len(y)+1):
    for j in range(1, len(x)+1):
        if y[i-1] != x[j-1]:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
        elif y[i-1] == x[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
print(LCS[-1][-1])