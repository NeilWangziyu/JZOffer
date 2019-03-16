def main():
    T = int(input().strip())
    left = 1024 - T
    coin1 = left // 64
    left = left % 64
    coin2 = left // 16
    left = left % 16
    coin3 = left // 4
    left = left % 4
    result = coin1 + coin2 + coin3 + left
    print(result)
main()