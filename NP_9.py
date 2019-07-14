def main():
    n = int(input().strip())
    list_tem = [str(i) for i in range(1, n+1)]
    res = []

    while(list_tem):
        res.append(list_tem.pop(0))
        if not list_tem:
            break
        list_tem.append(list_tem.pop(0))


    print(" ".join(res))

main()