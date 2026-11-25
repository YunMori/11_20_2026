#10814
N = int(input())
table = []
for _ in range(N):
    age,name = input().split()
    table.append([int(age),name])
table.sort(key= lambda x:x[0])#int,str 자료형에서 정렬할때 int 기준으로
# print(table)
for i in range(N):
    print(table[i][0],table[i][1])