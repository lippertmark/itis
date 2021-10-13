c = 0
a = int(input())
now = a
a = int(input())
ans = 0
while a!=0:
    if a == now:
        c+=1
    else:
        if ans<c:
            ans = c
        c = 1
        now = a
    a = int(input())
print(ans)