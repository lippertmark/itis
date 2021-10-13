a = int(input())
b = int(input())
sum = a + b
c = ((a - b) ** 2) ** 0.5
print(int((sum - c) // 2 + c))
