def matrix_multiply(A, B, mod):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod,
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod,
        ],
    ]

def matrix_power(matrix, n, mod):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base, mod)
        base = matrix_multiply(base, base, mod)
        n //= 2

    return result

def fibonacci_mod(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_power(F, n - 1, mod)
    return result[0][0]

# 입력을 받습니다
n = int(input())

# 1,000,000으로 나눈 나머지를 구합니다
mod = 1000000
print(fibonacci_mod(n, mod))