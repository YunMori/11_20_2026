#11399
N = int(input())
Time = list(map(int,input().split()))
Time.sort()
Name = []
Sum_List = []
for i in range(len(Time)):
    Name.append(Time[i])
    Sum_List.append(sum(Name))
print(sum(Sum_List))