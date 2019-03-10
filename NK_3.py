# def main():
#     while(True):
#         try:
#             input_string = input().strip()
#             if not input_string:
#                 return
#
#             input_string = input_string.split()
#             lo = int(input_string[0])
#             hi = int(input_string[1])
#             tem = []
#             if lo >= hi:
#                 print(0)
#             else:
#                 for i in range(lo, hi + 1):
#                     i_old = i
#                     length = len(str(i))
#                     res = 0
#                     while (i):
#                         res += (i % 10) ** length
#                         i = i // 10
#                     if res == i_old:
#                         tem.append(res)
#                 if not tem:
#                     print("no")
#                 else:
#                     print(" ".join(tem))
#         except:
#             return
# main()

# import sys
# def main():
#     for line in sys.stdin:
#         input_string = sys.stdin.readline().strip()
#         lo = int(input_string[0])
#         hi = int(input_string[1])
#         tem = []
#         if lo >= hi:
#             print("no")
#         else:
#             for i in range(lo, hi + 1):
#                 i_old = i
#                 length = len(str(i))
#                 res = 0
#                 while (i):
#                     res += (i % 10) ** length
#                     i = i // 10
#                 if res == i_old:
#                     tem.append(res)
#             if not tem:
#                 print("no")
#             else:
#                 print(" ".join(tem))
#
#  main()
