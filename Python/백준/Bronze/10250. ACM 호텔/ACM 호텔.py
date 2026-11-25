T = int(input())  # 테스트 케이스 수
for _ in range(T):
    H, W, N = map(int, input().split())
    
    # 방 번호 계산
    floor = (N - 1) % H + 1  # 층수는 N을 H로 나눈 나머지 + 1
    room = (N - 1) // H + 1  # 호수는 N을 H로 나눈 몫 + 1
    
    # 결과 출력 (방 번호 형식: 층수 + 호수)
    print(f"{floor}{room:02d}")