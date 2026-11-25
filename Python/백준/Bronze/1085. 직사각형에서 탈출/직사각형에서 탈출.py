x,y,w,h = map(int, input().split())
len = []
len.append(w-x)
len.append(h-y)
len.append(x)
len.append(y)
print(min(len))