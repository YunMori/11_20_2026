#4375 04/16
while True:
    try:
        n = int(input())
        a = 0
        for i in range(n+1):
            a+=10**i
            if a%n == 0:
                break
        print(i+1)
    except:
        break
