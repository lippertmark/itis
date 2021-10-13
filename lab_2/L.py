x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (y2 - y1 >= abs(x2 - x1) and y2 > y1 and ((x2 % 2 == x1 % 2 and (y2 - y1) % 2 == 0) or (x1 % 2 != x2 % 2 and (y2 - y1) % 2 != 0))):
    print('YES')
else:
    print('NO')