n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
res = 0
for each in a:
    for ele in b:
        tem = each + ele
        res ^= tem
print(res)


