#4673
def D (i):
    I = i
    A = list(map(int,str(I)))
    for n in A:
        I += n
    return I

original = []
D_list = []
for o in range(1,10001):
    original.append(o)
for i in original:
    D_list.append(D(i))
D_list = set(D_list)
for x in D_list:
    if x <= 10000:
        original.pop(original.index(x))
for a in original:
    print(a)