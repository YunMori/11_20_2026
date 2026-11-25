import sys
input = sys.stdin.readline

N = int(input())
ls = [tuple(map(int, input().split())) for _ in range(N)]
ls.sort()

start, last_y = ls[0]
answer = last_y - start

for i in range(1, N):
    cur_x, cur_y = ls[i]

    if cur_x > last_y:
        # 떨어진 선분이면 전체 길이를 더한다
        answer += cur_y - cur_x
        last_y = cur_y
    elif cur_y > last_y:
        # 겹치면서 오른쪽으로 늘어났으면 늘어난 길이만 더한다
        answer += cur_y - last_y
        last_y = cur_y

print(answer)