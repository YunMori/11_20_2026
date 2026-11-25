def is_group_word(word):
    seen_chars = set()
    last_char = ''
    
    for char in word:
        if char != last_char:
            if char in seen_chars:
                return False
            seen_chars.add(char)
            last_char = char
    return True

def count_group_words(words):
    count = 0
    for word in words:
        if is_group_word(word):
            count += 1
    return count

# 입력 받기
N = int(input())
words = [input().strip() for _ in range(N)]

# 그룹 단어 개수 출력
print(count_group_words(words))