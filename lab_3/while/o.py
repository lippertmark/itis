a = int(input())
mx = a
c = 1
a = int(input())
while a!=0:
    if a == mx:
        c+=1
    elif a>mx:
        mx = a
        c = 1
    a = int(input())
print(c)