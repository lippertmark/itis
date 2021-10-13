a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if (a1 > b1):
    k=a1
    a1=b1
    b1=k

if (b1 > c1):
    z= b1
    b1= c1
    c1= z
if (a1 > b1):
    i = a1
    a1 = b1
    b1 = i

if (a2 > b2):
    m = a2
    a2 = b2
    b2 = m
if (b2 > c2):
    a = b2
    b2 = c2
    c2 = a
if (a2 > b2):
    v = a2
    a2 = b2
    b2 = v
if ((a1==a2) and (b1==b2) and (c1==c2)):
    print ('Boxes are equal')
else:
    if ((a1 >= a2) and (b1 >= b2) and (c1 >= c2)):
        print('The first box is larger than the second one')
    elif ((a2 >= a1) and (b2 >= b1) and (c2 >= c1)):
        print('The first box is smaller than the second one')
    else:
        print('Boxes are incomparable');