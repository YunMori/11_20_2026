#11651
N = int(input())
table = []
for _ in range(N):
    x,y = map(int,input().split())
    table.append([x,y])
table.sort(key= lambda x : (x[1],x[0]))
for i in range(N):
    print(table[i][0],table[i][1])