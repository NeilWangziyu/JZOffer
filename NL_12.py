def main():
    def checkword(word):
        list_of_word = list(word)
        i, j, k, l = 0, 1, 2, 3
        length = len(list_of_word)

        if length < 3:
            return word
        while k < length:
            if list_of_word[i] == list_of_word[j] and list_of_word[j] == list_of_word[k]:
                list_of_word = list_of_word[:k] + list_of_word[k + 1:]
                length -= 1
            elif l < length:
                if list_of_word[i] == list_of_word[j] and list_of_word[k] == list_of_word[l]:
                    list_of_word = list_of_word[:k] + list_of_word[k + 1:]
                    length -= 1
                else:
                    i += 1
                    j += 1
                    k += 1
                    l += 1
            else:
                i += 1
                j += 1
                k += 1
                l += 1
        res_word = ''.join(list_of_word)
        return res_word


    N = int(input().strip())
    for i in range(N):
        string = input().strip()
        print(checkword(string))

main()


