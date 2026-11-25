#11659
import sys
def sumery(prefix,i,j,result = 0):
    if i == 1:
        result = prefix[j-1]
        return result
    result = prefix[j-1] - prefix[i-2]
    return result

Numbers, Sum_Numbers = map(int,sys.stdin.readline().split())

Numbers_List = list(map(int,sys.stdin.readline().split()))
prefix = []
prefix_N = 0
for x in Numbers_List:
    prefix_N += x
    prefix.append(prefix_N)
for _ in range(Sum_Numbers):
    i, j = map(int,sys.stdin.readline().split())
    print(sumery(prefix,i,j))