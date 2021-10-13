n = int(input())
for i in range(10**n,0,-1):
    if len(str(i)) == n and i%2 == 1:
        print(i, end=' ')