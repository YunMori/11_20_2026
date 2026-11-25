A = set()
for i in range(10):
    N = int(input())
    N = N % 42
    A.add(N)
print(len(A))