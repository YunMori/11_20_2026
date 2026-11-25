#2920
code = input()
table = '8 7 6 5 4 3 2 1'
sort_table = '1 2 3 4 5 6 7 8'
if code == table:
    print('descending')
elif code == sort_table:
    print('ascending')
else:
    print('mixed')