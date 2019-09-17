def main():
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())

    A = []
    for _ in range(x):
        input_num = input().strip().split()
        input_x = list(map(int, input_num))
        A.append(input_x)

    B = []
    for _ in range(y):
        input_num = input().strip().split()
        input_x = list(map(int, input_num))
        B.append(input_x)

    print(A)
    print(B)

    # res = [[0 for _ in range(len(B[0]))] for _ in range(len(A[0]))]
    # for i in range(len(A)):
    #     for j in range(len(B[0])):
    #         for k in range(len(B)):
    #             res[i][j] += A[i][k]*B[k][j]

    m, n, l = len(A), len(A[0]), len(B[0])
    res = [[0 for _ in range(l)] for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if A[i][k]:
                for j in range(l):
                    res[i][j] += A[i][k] * B[k][j]

    for each in res:
        each_str = map(str, each)
        print(" ".join(each_str))

main()