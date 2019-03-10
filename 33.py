# 后序遍历
def VerifySquenceOfBST(sequence):
    if not sequence:
        return True
    root = sequence[-1]
    i = 0
    while(sequence[i] < root):
        i += 1
    left = sequence[:i]
    right = sequence[i:-1]
    for each in right:
        if each < root:
            return False
    return VerifySquenceOfBST(left) and VerifySquenceOfBST(right)



if __name__ == "__main__":
    sequence = [5,7,6,9,11,10,8]
    print(VerifySquenceOfBST(sequence))
    sequence = [7, 4, 6, 5]
    print(VerifySquenceOfBST(sequence))