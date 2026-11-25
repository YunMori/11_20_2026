#1436
N = int(input())
D_List = []
List = list(map(str,range(666,3000000)))
# print(List)
for i in List:
    if '666' in i:
        D_List.append(i)
print(D_List[N-1])
