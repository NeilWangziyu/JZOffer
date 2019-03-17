class Solution():
    def all_arrange(self, str):
        if len(str) <= 1:
            return [str]
        else:
            res = []
            for i in range(len(str)):
                init = str[i]
                left = str[:i] + str[i+1:]
                for tem_list in self.all_arrange(left):

                    res.append(init + tem_list)
        return res



    def all_subset(self, str):
        res = []
        def DFS(index, depth, list):
            res.append(list)
            if index >= depth:
                return
            else:
                for i in range(index, depth):
                    DFS(i+1, depth, list+[str[i]])
        DFS(0, len(str), [])
        print(res)







if __name__ == "__main__":
    str = "abc"
    s = Solution()
    print(s.all_arrange(str))
    print(s.all_subset(str))
