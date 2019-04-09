import math
def main():
    A, N = list(map(int,input().split()))
    B = 0
    t = 0
    while(t <= N):
        t += 2**B
        B += 1
    print(B - 1 + math.ceil( A / ( 2 ** (B - 1))))
main()
