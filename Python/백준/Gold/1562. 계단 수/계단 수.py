import sys


def solve():
    N = int(input())
    MOD = 1_000_000_000

    if N < 10:
        print(0)
        return

    dp = [[0] * 1024 for _ in range(10)]

    for j in range(1, 10):
        dp[j][1 << j] = 1

    for i in range(2, N + 1):
        new_dp = [[0] * 1024 for _ in range(10)]
        for j in range(10):
            for mask in range(1024):
                if dp[j][mask] == 0:
                    continue
                val = dp[j][mask]

                if j - 1 >= 0:
                    nj = j - 1
                    nmask = mask | (1 << nj)
                    new_dp[nj][nmask] = (new_dp[nj][nmask] + val) % MOD
                if j + 1 <= 9:
                    nj = j + 1
                    nmask = mask | (1 << nj)
                    new_dp[nj][nmask] = (new_dp[nj][nmask] + val) % MOD
        dp = new_dp

    full_mask = (1 << 10) - 1 
    ans = 0
    for j in range(10):
        ans = (ans + dp[j][full_mask]) % MOD

    print(ans)


solve()