a = int(input())
b = int(input())
c = int(input())

if a<b and a<c:
    print(a, end=' ')
elif b<c:
    print(b, end=' ')
    b = a
else:
    print(c, end=' ')
    c = a
if b>c:
    print(c,b)
else:
    print(b,c)
