def main():
    # 20%
    n = int(input().strip())
    people = []
    for i in range(n):
        ab = input().strip().split()
        people.append((i, int(ab[0]), int(ab[1])))

    checked = [False for _ in range(n)]
    occupied = [False for _ in range(n)]
    people_a_list = sorted(people, key=lambda x:x[1], reverse=True)
    people_b_list = sorted(people, key=lambda x:x[2], reverse=True)

    i = 0
    index_a = 0
    j = n - 1
    index_b = 0
    res = 0

    while(i <= j):
        while(i < n and occupied[i] == True):
            i += 1
        while(j >= 0 and occupied[j] == True):
            j -= 1
        if (i > j):
            break
        while(index_a < n and checked[people_a_list[index_a][0]] == True):
            index_a += 1
        while(index_b < n and checked[people_b_list[index_b][0]] == True):
            index_b += 1

        if index_a >= n or index_b >= n:
            break

        if (i * people_a_list[index_a][1] + (n-1-i)*people_a_list[index_a][2]) <= (j * people_b_list[index_b][1] + (n-1-j)*people_b_list[index_b][2]):
                res += (i * people_a_list[index_a][1] + (n-1-i)*people_a_list[index_a][2])
                checked[people_a_list[index_a][0]] = True
                occupied[i] = True
                i += 1
                index_a += 1
        else:
            res +=  (j * people_b_list[index_b][1] + (n-1-j)*people_b_list[index_b][2])
            checked[people_b_list[index_b][0]] = True
            occupied[j] = True
            j -= 1
            index_b += 1


    print(res)
main()

