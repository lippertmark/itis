c = 0
a = int(input())
pr = 0
while a!=0:
    if a>=c:
        pr = c
        c = a
    a = int(input())
print(pr)