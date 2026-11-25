N = int(input())
i = 1
End_line = 1
while N != 1:
    if N <= End_line:
        break
    End_line = End_line+(6*i)
    i += 1
print(i)