#2630
result = []
def split(x,y,N):
    color = table[y][x]
    for i in range(y, y+N):
        for j in range(x, x+N):
            if color != table[i][j]:
                split(x,y,N//2)
                split(x+N//2,y,N//2)
                split(x,y+N//2,N//2)
                split(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)
        
N = int(input())

table = []
for _ in range(N):
    t = list(map(int, input().split()))
    table.append(t)
split(0,0,N)
print(result.count(0))
print(result.count(1))