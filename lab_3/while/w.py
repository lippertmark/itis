n = int(input())
ans = ''
now_del = 2
while now_del * now_del <= n:
    if n % now_del == 0:
        c = 0
        while n % now_del == 0:
            n //= now_del
            c += 1
        if ans != '':
            ans += '*'
        if c ==1:
            ans+=str(now_del)
        else:
            ans += str(now_del) + '^' + str(c)
    else:
        now_del += 1
if n > 1:
    if len(ans) == 0:
        ans += str(n)
    else:
        ans += '*' + str(n)
print(ans)
