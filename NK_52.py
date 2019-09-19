n = int(input())
s = list(map(int, input().split()))

def candy(s,n):
    if sum(s) % n != 0:
        return -1
    tar = sum(s) / n
    s.sort()
    sumn = 0
    for i in s:
        if tar % 2 != i %2:
            return -1
        if i < tar:
            sumn += abs(tar-i) // 2
    return sumn

res = candy(s, n)
print(int(res))