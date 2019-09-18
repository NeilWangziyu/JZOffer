import copy

s = input().split()
n = int(s[0])
m = int(s[1])

g = []
for i in range(n):
    gtemp = []
    gtemp[:] = map(int, input().split())
    g.append(gtemp)

b = []
for i in range(m):
    b.append(int(input()))

def soccer(b, g):
    def dfs(b, g):
        res = []
        for ball in b:
            for gate in g:
                if ball >= gate[0] and ball <= gate[1]:
                    btemp = copy.copy(b)
                    gtemp = copy.copy(g)
                    btemp.remove(ball)
                    gtemp.remove(gate)
                    remscore = dfs(btemp, gtemp)
                    res.append(remscore + 1)
                if ball > gate[1]:
                    break

        if not res:
            return 0
        else:
            return max(res)

    g.sort(key=lambda x: x[1], reverse=True)
    return dfs(b, g)

print(soccer(b, g))