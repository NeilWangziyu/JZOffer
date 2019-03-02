def hasPath(matrix, str):
    if not matrix:
        return False

    visited = [[False for  _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == str[0]:
                if check_point(i, j, matrix, visited, 1, str):
                    return True
    return False



def check_point(i, j, matrix, visited, index, str):
    if index > len(str)-1:
        return True
    visited[i][j] = True
    if i > 0:
        if not visited[i-1][j]:
            if matrix[i-1][j] == str[index]:
                if check_point(i-1, j, matrix, visited, index+1, str):
                    return True

    if i < len(matrix)-1:
        if not visited[i+1][j]:
            if matrix[i+1][j] == str[index]:
                if check_point(i+1, j, matrix, visited, index+1, str):
                    return True
    if j > 0:
        if not visited[i][j-1]:
            if matrix[i][j-1] == str[index]:
                if check_point(i, j-1, matrix, visited, index+1, str):
                    return True
    if j < len(matrix[0])- 1:
        if not visited[i][j+1]:
            if matrix[i][j+1] == str[index]:
                if check_point(i, j+1, matrix, visited, index+1, str):
                    return True
    return False



if __name__ == "__main__":
    matrix = [["a", "b", "t", "g"], ["c", "f", "c", "s"], ["j", "d", "e", "h"]]
    str1 = "bfce"
    str2 = "abfb"
    print(hasPath(matrix, str1))
    print(hasPath(matrix, str2))