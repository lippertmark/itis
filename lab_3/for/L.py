n = int(input())
ans = 0
fac_now = 1
fac_pred = 1
for i in range(1, n+1):
    fac_now= fac_pred*i
    ans+=fac_now
    fac_pred = fac_now
print(ans)