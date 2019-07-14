# https://leetcode-cn.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        test_stack = []
        index = 0
        for each in pushed:
            test_stack.append(each)
            while (test_stack and test_stack[-1] == popped[index]):
                test_stack.pop()
                index += 1
        return len(test_stack) == 0
