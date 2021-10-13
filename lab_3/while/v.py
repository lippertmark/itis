c = 1
a = int(input())
pred = a
a = int(input())
now = 1
ans = 0
while a!=0:
    if now == 1:
        if pred<a:
            c+=1
        elif pred>a:
            now = -1
            ans = max(ans, c)
            c = 2
        else:
            ans = max(ans, c)
            c = 2
            pred = 0
            a = int(input())
            if a == 0:
                c = 0
                break
            if a>pred:
                now = 1
            else:
                now = -1
    else:
        if pred>a:
            c+=1
        elif pred>a:
            now = -1
            ans = max(ans, c)
            c = 2
        else:
            ans = max(ans, c)
            c = 2
            pred = 0
            a = int(input())
            if a == 0:
                c = 0
                break
            if a > pred:
                now = 1
            else:
                now = -1
    pred = a
    a = int(input())
ans = max(ans, c)
print(ans)