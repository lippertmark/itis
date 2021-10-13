n = int(input())
sum = 0
for i in range(1,n+1):
    sum +=i
sum_now = 0
for i in range(n-1):
    sum_now+=int(input())
print(sum-sum_now)