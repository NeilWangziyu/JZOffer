def count(x1, y1, x2, y2):
    w = 0
    b = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if (i+j)//2==0:
                w += 1
            else:
                b += 1
    return w, b

def cover(A, B, C, D, E, F, G, H):
    list_x = [A, C, E, G]
    list_x.sort()
    list_y = [B, D, F, H]
    list_y.sort()
    return list_x[1], list_y[1], list_x[2], list_y[2]


def main():
    T = int(input().strip())
    for i in range(T):
        n_m = input().strip().split(' ')
        n = int(n_m[0])
        m = int(n_m[1])
        init_w, init_b = count(1, 1, n, m)
        question1 = input().strip().split(' ')
        x0, y0, x1, y1 = int(question1[0]), int(question1[1]), int(question1[2]), int(question1[3])
        first_w, first_b = count(x0, y0, x1, y1)

        question2 = input().strip().split(' ')
        x00, y00, x11, y11 = int(question2[0]), int(question2[1]), int(question2[2]), int(question2[3])
        second_w, second_b = count(x00, y00, x11, y11)

        minx = max(x0, x00)
        miny = max(y0, y00)
        maxx = min(x1, x11)
        maxy = min(y1, y11)
        if minx > maxx or miny > maxy:
            x_c1, y_c1, x_c2, y_c2 = cover(x0, y0, x1, y1, x00, y00, x11, y11)
            w_cover, b_cover = count(x_c1, y_c1, x_c2, y_c2)
            area = (x_c2 - x_c1 + 1) * (y_c2 - y_c1 + 1)
            w_num = init_w + first_b - (area + second_w - w_cover)
            b_num = init_b - first_b + (area + second_w - w_cover)
            print("{} {}".format(min(w_num,b_num), max(w_num,b_num)))
        else:
            
            print("{} {}".format(init_w + first_b - second_w, init_b - first_b + second_w))
main()