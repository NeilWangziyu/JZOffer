class min_stack():
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return "empty"


    def push(self,item):
        if not self.stack:
            self.stack.append(item)
            self.min_stack.append(item)
        else:
            self.stack.append(item)
            if item < self.min_stack[-1]:
                min_num = item
            else:
                min_num = self.min_stack[-1]
            self.min_stack.append(min_num)



    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def print(self):
        print("stack", self.stack)
        print("min_stack", self.min_stack)


if __name__ == "__main__":
    s = min_stack()
    s.push(3)
    s.push(4)
    s.push(2)
    s.print()
    s.push(1)
    s.pop()
    s.pop()
    s.print()
    s.push(0)
    s.print()