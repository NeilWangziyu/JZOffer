# 用两个栈实现队列
# 用两个队列实现栈
class buildQueueByStack():
    def __init__(self):
        self.stack_a = []
        self.stack_b = []


    def equeue(self, val):
        self.stack_a.append(val)

    def dqueue(self):
        if not self.stack_a and not self.stack_b:
            print("empty queue")
            return None

        if self.stack_b:
            return self.stack_b.pop()
        else:
            while(self.stack_a):
                self.stack_b.append(self.stack_a.pop())
            return self.stack_b.pop()




    def print(self):
        print(self.stack_a)
        print(self.stack_b)




if __name__ == "__main__":
    s = buildQueueByStack()
    s.equeue(1)
    s.equeue(2)
    s.equeue(3)
    s.equeue(4)
    print(s.dqueue())
    s.equeue(5)
    s.equeue(6)
    s.equeue(7)

    print(s.dqueue())
    print(s.dqueue())
    print(s.dqueue())
    print(s.dqueue())
    print(s.dqueue())