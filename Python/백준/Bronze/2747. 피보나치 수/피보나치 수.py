N = int(input())
i = [0,1]
for a in range(N-1):
    x = i[a]+i[a+1]
    i.append(x)
print(i[-1])