# n, b = map(int, input().split())

# #진수변환
# def solution(n, b):
#     rev_base = ''

#     while n > 0:
#         n, mod = divmod(n, b)
#         rev_base += str(mod)

#     return rev_base[::-1] 
#     # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

# result = str (solution(n,b)[::-1])

# v = [result[i:i+2] for i in range(0, len(result),2)]#문자열 2자리씩 나누기
# real = []
# for a in v:
#     a = int(a)
#     if a == 10:
#         a='A'
#     elif a==11:
#         a='B'
#     elif a==12:
#         a='C'
#     elif a==13:
#         a='D'
#     elif a==14:
#         a='E'
#     elif a==15:
#         a='F'
#     elif a==16:
#         a='G'
#     elif a==17:
#         a='H'
#     elif a==18:
#         a='I'
#     elif a==19:
#         a='J'
#     elif a==20:
#         a='K'
#     elif a==21:
#         a='L'
#     elif a==22:
#         a='M'
#     elif a==23:
#         a='N'
#     elif a==24:
#         a='O'
#     elif a==25:
#         a='P'
#     elif a==26:
#         a='Q'
#     elif a==27:
#         a='R'
#     elif a==28:
#         a='S'
#     elif a==29:
#         a='T'
#     elif a==30:
#         a='U'
#     elif a==31:
#         a='V'
#     elif a==32:
#         a='W'
#     elif a==33:
#         a='X'
#     elif a==34:
#         a='Y'
#     elif a==35:
#         a='Z'
#     real.append(a)

# real_answer = ''.join(real)
# print(real_answer)

def convert_to_base(N, B):
    digits = []
    while N > 0:
        remainder = N % B
        if remainder >= 10:
            digits.append(chr(55 + remainder))  # 10 이상일 경우 알파벳으로 변환 
                                 #유니코드 활용 
        else:
            digits.append(str(remainder))  # 10 미만일 경우 숫자로 변환
        N //= B
    return ''.join(digits[::-1])  # 역순으로 변환하여 결과 출력

# 입력 받기
N, B = map(int, input().split())
# 진법 변환 결과 출력
print(convert_to_base(N, B))