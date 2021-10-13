k = int(input())
c = 0
for i in range(1, k+1):
    if str(i) == str(i)[::-1]:
        c+=1
print(c)