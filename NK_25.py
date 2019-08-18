n,m = list(map(int,input().split()))

def getChildCount(pre,mx):
    ans = 1
    p = 10
    while pre * p <= mx:
        if pre * p + p - 1 <= mx:
            ans += p
        else:
            ans += mx - pre * p + 1
        p *= 10
    return ans

def find(m,mx):
    ans = 1
    while m != 0:
        v = getChildCount(ans, mx)
        if v < m:
            ans += 1
            m -= v
            continue
        if m == 1:
            break
        ans *= 10
        m -= 1
    return ans

print(find(m,n))

# 查找字典序排数中具体位置的数

# http://www.lyqhahaha.xyz/P/64/