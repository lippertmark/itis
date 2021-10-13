a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
for x in range(0, 1000):
    if (x-e != 0) and (a*x**3 +b*x**2 +c*x+d)/(x-e) == 0:
        count +=1
print(count)