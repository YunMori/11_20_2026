#1978
N = int(input())
PN = list(map(int, input().split()))
count = 0
for i in PN:
    i_counter = 0
    for a in range(1,i+1):
        if i%a == 0 and i != 1:
            i_counter += 1
    if i_counter == 2:
        count += 1
print(count)