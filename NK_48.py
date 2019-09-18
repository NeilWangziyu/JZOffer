def count(a, b, k):
    c = 0
    for i in range(min(a,b), max(a,b)+1):
        if(i%k==0 and div2(i, k)):
            c += 1
    return c

def div2(c, k):
    for i in range(2, k):
        if(c % i == 0):
            return False
    return True

a_b_k = input().strip().split()
a = int(a_b_k[0])
b = int(a_b_k[1])
k = int(a_b_k[2])
c = count(a,b,k)
print(c)