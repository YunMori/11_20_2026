import math


def main():
    N, M, K = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(1, N + 1):
        arr[i] = int(input())

    size = 1
    while size < N:
        size <<= 1

    tree = [0] * (2 * size)

    for i in range(1, N + 1):
        tree[size + i - 1] = arr[i]

    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    def update(idx, val):
        pos = size + idx - 1
        tree[pos] = val
        pos >>= 1
        while pos >= 1:
            tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
            pos >>= 1

    def query(l, r):
        res = 0
        l = size + l - 1
        r = size + r - 1
        while l <= r:
            if l & 1:
                res += tree[l]
                l += 1
            if not (r & 1):
                res += tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

    result = []
    for _ in range(M + K):
        line = input().split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        if a == 1:
            update(b, c)
        else:
            result.append(query(b, c))

    print('\n'.join(map(str, result)))


main()