f_pred = 1
f_pred_pred = 0
n = int(input())
if n == 0:
    print(0)
elif n==1:
    print(1)
else:
    i = 1
    f_now = 1
    while f_now<n:
        f_now = f_pred+f_pred_pred
        f_pred_pred = f_pred
        f_pred = f_now
        i+=1
    if f_now== n:
        print(i)
    else:
        print(-1)
