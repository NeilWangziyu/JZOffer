import numpy as np
def Fibonacci_Matrix_tool(n): # 递归求解,速度慢与直接求方
    Matrix = np.matrix('1 1 0 0;1 0 0 0;0 1 0 0;0 0 1 0')
    if n == 1:
        return Matrix
    if n == 2:
        return pow(Matrix, 2)
    elif n % 2 == 1:
        return Fibonacci_Matrix_tool((n - 1) / 2) ** 2 * Matrix
    else:
        return Fibonacci_Matrix_tool(n / 2) ** 2


def Fibonacci_Matrix_tool2(n):
    Matrix = np.matrix('1 1 0 0;1 0 0 0;0 1 0 0;0 0 1 0')
    return pow(Matrix, n) # pow函数速度快于 使用双星号 "**"


def Fibonacci_Matrix(n):
    result_list = []
    for i in range(1, n):
        print(np.array([1,2,3,4]) * np.array(Fibonacci_Matrix_tool2(i))[0][0])
        # result_list.append(np.array([1,2,3,4]) * np.array(Fibonacci_Matrix_tool2(i)))
    return result_list


print(Fibonacci_Matrix(20))