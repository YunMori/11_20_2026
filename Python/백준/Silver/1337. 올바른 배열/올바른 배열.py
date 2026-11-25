#1337 Oct 19, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N = int(sys.stdin.readline())

nums = list(int(sys.stdin.readline()) for _ in range(N))
nums = sorted(nums)

answer = list()
for i in nums:
    end = i+4
    count = 0
    for j in range(i, i+5):
        if j in nums:
            continue
        else:
            count += 1
    answer.append(count)
print(min(answer))