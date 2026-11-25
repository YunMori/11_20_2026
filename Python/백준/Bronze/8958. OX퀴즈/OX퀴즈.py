#8958
T = int(input())
for teat_case in range(1,T+1):
    M = input()
    M = list(map(str,M))
    answer = 0
    count = 0
    c = 0
    for i in M:
        if i == 'X' :
            answer += count
            count = 0
            c = 0
        if i =='O':
            c +=1
            count = count+c
    answer += count
    print(answer)