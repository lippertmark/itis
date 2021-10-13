x = int(input())
y = int(input())
if x%(y-x+1) == 0:
    print('YES')
else:
    print('NO')
