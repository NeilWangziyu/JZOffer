def func(arr):
    n=len(arr)
    for i in range(1,n//2+1):
        if n % i == 0:
            a = arr[:i]
            j = i
            while j<n and arr[j:j+i]==a:
                j += i
            if j == n:
                return i 
    return 0

arr = input().strip()

tmp = func(arr)
if tmp == 0 :
    for i in range(len(arr)):
        print('0',end='')
else:
    cnt = 1
    for i in range(len(arr)):
        if cnt == tmp:
            print('1',end='')
            cnt = 1
        else:
            cnt+=1
            print('0',end='')



------------------
# import sys
#
# string = sys.stdin.readline().rstrip()
#
# res = [0 for i in string]
#
# for i in range(len(string)//2+1, 0, -1):
#     is_dup = True
#     for j in range(i):
#         if string[j] != string[j+i]:
#             is_dup = False
#             break
#     if is_dup:
#         break
#
# if is_dup:
#     for j in range(i-1, len(string), i):
#         res[j] = 1
#
# res = map(str, res)
# output = ''.join(res)
# print(output)