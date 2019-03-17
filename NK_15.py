def main():
    N = int(input().strip())
    x_p_list = []
    x_n_list = []
    for i in range(N):
        x_a = input().strip().split()
        if int(x_a[0]) > 0:
            x_p_list.append([int(x_a[0]), int(x_a[1])])
        else:
            x_n_list.append([int(x_a[0]), int(x_a[1])])

    x_p_list = sorted(x_p_list, key=lambda x: x[1])
    x_n_list = sorted(x_n_list, key=lambda x: x[1])
    n_length = len(x_n_list)
    p_length = len(x_p_list)
    if n_length == p_length:
        res = 0
        for i in range(p_length):
            res += x_p_list[i][1]
            res += x_n_list[i][1]
            print(res)
    elif n_length > p_length:
        res = 0
        for i in range(p_length):
            res += x_p_list[i][1]
            res += x_n_list[i][1]

        print(res + x_n_list[p_length][1])

    else:
        res = 0
        for i in range(n_length):
            res += x_p_list[i][1]
            res += x_n_list[i][1]
        print(res + x_p_list[n_length][1])

main()

# -------------
n = int(input())
x = []
a = []
for _ in range(n):
    xi,ai = map(int,input().split())
    x.append(xi)
    a.append(ai)
appletree = list(zip(x,a))
appletree = sorted(appletree)
below = 0
over = 0
start = -1
for i in range(n):
    if appletree[i][0] < 0:
        below += 1
    else:
        if start == -1:
            start = i
        over += 1
length = min(below,over)
res = 0
for k in range(start,start+length):
    res += appletree[k][1]
for k in range(start-length,start,1):
    res += appletree[k][1]
if below > over:
    res += appletree[start-length-1][1]
else:
    res += appletree[start+length][1]
print(res)