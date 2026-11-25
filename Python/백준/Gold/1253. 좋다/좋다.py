#1043 Oct 19, 2025
import sys
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (2).txt','rt')

N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

cnt = 0
for g in range(N):
    target = nums[g]
    i, j = 0, N-1
    
    while i < j:
        if i == g:
            i += 1
            continue
        if j == g:
            j -= 1
            continue
        total = nums[i] + nums[j]
        
        if total == target:
            cnt += 1
            break
        elif total < target:
            i += 1
        else:
            j -= 1
print(cnt)