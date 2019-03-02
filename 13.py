def movingCount(threshold, row, col):
    if threshold < 0 or row < 0 or col < 0:
        return False

    visited = [[False for _ in range(col)] for _ in range(row)]
    count = movingCountCore(threshold, row, col, 0, 0, visited)
    return count

def movingCountCore(threshod, row, col, x, y, visited):
    count = 0
    if check(threshold, row, col, x, y, visited):
        print(x, y)
        visited[x][y] = True
        count = 1 + movingCountCore(threshod, row, col, x+1, y, visited) + movingCountCore(threshod, row, col, x-1, y, visited) + movingCountCore(threshod, row, col, x, y+1, visited) + movingCountCore(threshod, row, col, x, y-1, visited)
    return count


def check(threshold, row, col, x, y, visited):
    if x > row - 1 or y > col - 1 or x < 0 or y < 0 or visited[x][y] == True:
        return False
    if get_num(x, y) > threshold:
        return False
    else:
        return True



def get_num(x, y):
    count = 0
    while(x):
        count += x % 10
        x = x // 10
    while(y):
        count += y % 10
        y = y // 10
    return count



if __name__ == "__main__":
    threshold = 10
    init_x = 30
    init_y = 40
    print(movingCount(threshold, init_x, init_y))
