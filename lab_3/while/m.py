c = 0
i = 0
a = int(input())
while a!=0:
    if i!=0:
        if a>pred:
            c+=1
    pred = a
    i+=1
    a = int(input())
print(c)