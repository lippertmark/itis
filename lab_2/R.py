h_sk = int(input())
w_sk = int(input())
l_sk = int(input())
h = int(input())
w = int(input())
l = int(input())

c1 = (h_sk // h) * (w_sk // w) * (l_sk // l)
c2 = (h_sk // h) * (w_sk // l) * (l_sk // w)
c3 = (h_sk // w) * (w_sk // h) * (l_sk // l)
c4 = (h_sk // w) * (w_sk // l) * (l_sk // h)
c5 = (h_sk // l) * (w_sk // w) * (l_sk // h)
c6 = (h_sk // l) * (w_sk // h) * (l_sk // w)

if c1 >= c2 and c1 >= c3 and c1 >= c4 and c1 >= c5 and c1 >= c6:
    print(c1)
elif c2 >= c1 and c2 >= c3 and c2 >= c4 and c2 >= c5 and c2 >= c6:
    print(c2)
elif c3 >= c1 and c3 >= c2 and c3 >= c4 and c3 >= c5 and c3 >= c6:
    print(c3)
elif c4 >= c1 and c4 >= c2 and c4 >= c3 and c4 >= c5 and c4 >= c6:
    print(c4)
elif c5 >= c1 and c5 >= c3 and c5 >= c4 and c5 >= c2 and c5 > c6:
    print(c5)
else:
    print(c6)
