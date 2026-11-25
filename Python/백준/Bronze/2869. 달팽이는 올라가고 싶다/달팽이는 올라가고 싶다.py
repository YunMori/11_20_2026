A, B, V = map(int, input().split())
if V <= A:
    print(1)
else:
    import math
    days = math.ceil((V - A) / (A - B)) + 1
    print(days)