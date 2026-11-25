#2577
A_B_C = []
ABC = 1
for _ in range(3):
    N = int(input())
    A_B_C.append(N)
for i in A_B_C:
    ABC *= i
ABC = list(map(int,str(ABC)))

for i in range(10):
    print(ABC.count(i))