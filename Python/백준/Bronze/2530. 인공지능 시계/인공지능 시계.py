A,B,C = map(int,input().split())
D = int(input())
C = C+(B*60)+(A*60*60)
time = C+D
second = time%60
minute = (time//60)%60
hour = time//60//60
if hour >= 24:
    time = (hour//24)*60*60
    second = second+(time%60)
    minute = minute+((time//60)%60)
    hour = hour%24
print(hour,minute,second)