# def main():
#     inputs = input().strip()
#     list_N = inputs.split(";")
#     inut_list = list_N[0]
#     N = int(list_N[1])
#     input_list = inut_list.split(",")
#     odd_list = []
#     even_list = []
#     for each in input_list:
#         if each.endswith("0") or each.endswith("2") or each.endswith("4") or each.endswith("6") or each.endswith("8") :
#             even_list.append(each)
#         else:
#             odd_list.append(each)
#     odd_list.sort()
#     even_list.sort()
#     res = (odd_list+even_list)[:N]
#     print(",".join(res))
# main()


import sys
string1 = sys.stdin.readline().rstrip()

string1 = string1.split(';')
N = int(string1[1])

string1 = string1[0]
string1 = string1.split(',')
odd = []
even = []
for i in string1:
    tmp = int(i)
    if tmp%2:
        odd.append(tmp)
    else:
        even.append(tmp)
even.sort(reverse=True)
if N<=len(even):
    res = even[:N]
else:
    res = even
    remain = N-len(even)
    odd.sort(reverse=True)
    res += odd[:remain]

res = map(lambda x:str(x),res)

s = ','.join(res)
print(s)