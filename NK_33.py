def main():
    a = input().strip().split(" ")

    t = int(a[0])
    k = int(a[1])

    max_one = 0

    ranges = []
    for i in range(t):
        a = input().strip().split(" ")
        tmp0 = int(a[0])
        tmp1 = int(a[1])
        max_one = max(max_one, tmp1)
        ranges.append([tmp0,tmp1])

    block = '0'*k

    solves = [{''}]

    for i in range(1,k):
        now_set = set()
        tmp = '1'*i
        now_set.add(tmp)
        solves.append(now_set)

    for i in range(k, max_one+1):
        now_set = set()
        for j in solves[i-1]:
            tmp0 = '1'+ j
            tmp1 = j+'1'
            now_set.add(tmp0)
            now_set.add(tmp1)
        for j in solves[i-k]:
            tmp0 = block + j
            tmp1 = j + block
            now_set.add(tmp0)
            now_set.add(tmp1)
        solves.append(now_set)

    for i in ranges:
        res = 0
        for j in range(i[0],i[1]+1):
            res += len(solves[j])
        print(res)

main()
