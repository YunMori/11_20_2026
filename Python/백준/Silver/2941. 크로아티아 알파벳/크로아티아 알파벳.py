H = 'c=','c-',' dz=' ,'d-' ,'lj' ,'nj' ,'s=' ,'z='
A = input()
if 'dz=' in A:
   A = A.replace('dz=','*')
   for i in H:
    A=A.replace(i,'*')
else:
    for i in H:
        A=A.replace(i,'*')
print(len(A))
