table = list(map(int,input().split()))
answer = 0
for i in table:
    answer = answer+(i**2)
print(answer%10)