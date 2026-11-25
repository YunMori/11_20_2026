# #7568
N = int (input())
h_list = []
for _ in range(N):
    x,y = map(int,input().split())
    h_list.append([x,y])
# h_list = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
for i in h_list:
    rank = 1
    for j in h_list:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end =' ')
    