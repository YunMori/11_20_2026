#10179
import math
T = int(input())
for _ in range(T):
    N= float(input())
    answer = round(N-(N*0.2),2)
    print(f'${answer:.2f}')