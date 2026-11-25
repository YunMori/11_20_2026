N = int(input())
for _ in range(N):
    a = input()
    b = list(a.split())
    for i in range(len(b)):
        b[i] = b[i][::-1]
    answer = ' '.join(b) 
    print(answer)