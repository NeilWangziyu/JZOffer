def LongestSubstringWithoutDuplication(str):
    if not str:
        return 0
    curLength = 0
    maxLength = 0

    store_list = [-1 for _ in range(26)]
    for i in range(len(str)):
        prev_index = store_list[ord(str[i]) - ord('a')]
        if prev_index == -1 or i - prev_index > curLength:
            curLength += 1
        else:
            if curLength > maxLength:
                maxLength = curLength
            curLength = i - prev_index

        store_list[ord(str[i]) - ord('a')] = i


    if curLength > maxLength:
        maxLength = curLength
    return maxLength



if __name__ == "__main__":
    str='arabcacfrabcdefghikkk'
    print(LongestSubstringWithoutDuplication(str))