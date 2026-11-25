# 입력된 다섯 줄의 단어들을 리스트로 저장
words = [input().strip() for _ in range(5)]

# 세로로 읽은 글자를 저장할 결과 문자열
result = []

# 최대 15개의 글자까지 존재할 수 있으므로 15번 반복
for i in range(15):
    for word in words:
        if i < len(word):  # 현재 단어의 i번째 글자가 있는 경우에만 추가
            result.append(word[i])

# 결과 리스트를 문자열로 변환하여 출력
print(''.join(result))