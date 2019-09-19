a_b = input().strip().split()
a = int(a_b[0])
b = int(a_b[1])

bias = 1e-7
low = 1.0
high = a

x = (low + high) / 2
while(abs(x**b - a) > bias):
    if x ** b > a:
        high = x
    else:
        low = x
    x = (low + high) / 2
print("%.6f" % x)