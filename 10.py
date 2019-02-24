import time
def Fibonacci(n):
    if n<=0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def Fibonacci_quick(n):
    if n<=0:
        return 0
    if n == 1:
        return 1

    fib_one = 1
    fib_two = 1
    res = 0
    for i in range(2, n):
        res = fib_one + fib_two
        fib_one = fib_two
        fib_two = res
    return res



if __name__ == "__main__":
    init = time.time()
    print(Fibonacci(30))
    print(time.time() - init)
    init = time.time()
    print(Fibonacci_quick(30))
    print(time.time() - init)