n = int(input())
sx = []
if n == 0:
    print(0)
for i in range(n):
    temp = list(map(int, input().strip().split()))
    sx.append(temp)

def second(elem):
    return elem[1]

sx.sort(key=lambda x:(x[1], x[0]))

A = []
B = []
sumB_b = 0
sumB_a = 0
for i in range(n):
    B.append(sx[i])
    sumB_a += sx[i][0]
    sumB_b += sx[i][1]
    for j in range(i+1, n):
        A.append(sx[j])
    if(len(A) > sumB_a):
        A = []
        continue
    else:
        print(sumB_b)
        break

