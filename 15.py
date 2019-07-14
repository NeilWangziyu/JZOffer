def NumberOF1(n):
    count = 0
    while(n):
        n = (n-1) & n
        count += 1
    return count


def quick_Sort(n):
    if len(n)<=1:
        return n
    else:
        pivo = n[0];less=[];more=[]
        for each in n[1:]:
            if each <= pivo:
                less.append(each)
            else:
                more.append(each)
        return quick_Sort(less) + [pivo] + quick_Sort(more)



if __name__ == "__main__":
    n = 15
    print(NumberOF1(n))
    list_t = [0,2,3,4,1,9,5,6,8,7]
    print(quick_Sort(list_t))