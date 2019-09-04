# # import json
# #
# # def main():
# #     input_string = ""
# #
# #     while (True):
# #         try:
# #             tem_input = input().strip()
# #         except:
# #             break
# #         input_string += tem_input
# #
# #     try:
# #         j = json.loads(input_string)
# #         print(0)
# #     except:
# #         print(1)
# #
# #     error = []
# #     stack = []
# #     large_parent = 0
# #     mid_parent = 0
# #
# #     in_yinhao = False
# #     for each in input_string:
# #         if each == "{":
# #             if in_yinhao:
# #                 error.append(4)
# #                 in_yinhao = False
# #                 while (stack and stack[-1] != "\""):
# #                     stack.pop()
# #                 if stack[-1] == "\"":
# #                     stack.pop()
# #
# #             stack.append(each)
# #             large_parent += 1
# #
# #         elif each == "\"":
# #             if in_yinhao:
# #                 while(stack and stack[-1] != "\""):
# #                     stack.pop()
# #                 if stack[-1] == "\"":
# #                     stack.pop()
# #             else:
# #                 stack.append(each)
# #                 in_yinhao = True
# #
# #         elif each == "[":
# #             if in_yinhao:
# #                 error.append(4)
# #                 in_yinhao = False
# #                 while (stack and stack[-1] != "\""):
# #                     stack.pop()
# #                 if stack[-1] == "\"":
# #                     stack.pop()
# #
# #             stack.append(each)
# #             mid_parent += 1
# #
# #         elif each == ",":
# #             if in_yinhao:
# #                 error.append(4)
# #                 in_yinhao = False
# #                 while (stack and stack[-1] != "\""):
# #                     stack.pop()
# #                 if stack[-1] == "\"":
# #                     stack.pop()
# #
# #
# #             stack.append(each)
# #
# #         elif each == "}":
# #             if in_yinhao:
# #                 error.append(4)
# #                 in_yinhao = False
# #                 while (stack and stack[-1] != "\""):
# #                     stack.pop()
# #                 if stack[-1] == "\"":
# #                     stack.pop()
# #             large_parent -= 1
# #             tem_output = ""
# #             while(stack and stack[-1]!= "{"):
# #                 if stack[-1] == "":
# #                     pass
# #
# #
# #
# #         elif each == "]":
# #             if in_yinhao:
# #                 error.append(4)
# #                 in_yinhao = False
# #                 while (stack and stack[-1] != "\""):
# #                     stack.pop()
# #                 if stack[-1] == "\"":
# #                     stack.pop()
# #
# #         else:
# #             stack.append(each)
# #
# #
# # main()
#
#
# import json
#
# def main():
#     input_string = ""
#
#     while (True):
#         try:
#             tem_input = input().strip()
#         except:
#             break
#         input_string += tem_input
#
#     try:
#         j = json.loads(input_string)
#         print(0)
#     except:
#         res = parser(input_string.split())
#         print(res)
#
# main()
#
#
# def parser(input_string):
#     find_error = set()
#     if not input_string:
#         return find_error
#     else:
#         if input_string[0] == "{" and input_string[-1] == "}":
#
#             c1 = 0
#             c2 = 0
#             init = 0
#             each_pairs = []
#             for index in range(len(input_string)):
#                 if input_string[index] == "[":
#                     c1 += 1
#                 elif input_string[index] == "{":
#                     c2 += 1
#                 elif input_string[index] == "]":
#                     c1 -= 1
#                 elif input_string[index] == "}":
#                     c2 -= 1
#                 else:
#                     if c1 == 0 and c2 == 0 and input_string[index] == ",":
#                         each_pairs.append(input_string[init:index])
#                         init = index + 1
#                     else:
#                         pass
#
#
#             for each_pair in each_pairs:
#                 each_key_value = each_pair.split(":")
#                 key = each_key_value[0].strip()
#                 value = each_key_value[1].strip()
#                 key_res = parser(key)
#                 value_res = parser(value)
#                 find_error.union(key_res)
#                 find_error.union(value_res)
#
#         elif input_string[0] == "{" and input_string[-1] != "}":
#             find_error.add(2)
#             res = parser(input_string + "}")
#             find_error.union(res)
#
#         elif input_string[0] != "{" and input_string[-1] == "}":
#             find_error.add(2)
#             res = parser("{" + input_string)
#             find_error.union(res)
#
#         elif input_string[0] == "[" and input_string[-1] == "]":
#
#             pass
#
#         elif input_string[0] == "[" and input_string[-1] != "]":
#             find_error.add(1)
#             res = parser(input_string + "]")
#             find_error.union(res)
#
#
#         elif input_string[0] != "[" and input_string[-1] == "]":
#             find_error.add(1)
#             res = parser("[" + input_string)
#             find_error.union(res)
#
#
#         elif input_string[0] == "\"" and input_string[-1] == "\"":
#             pass
#         elif input_string[0] == "\"" and input_string[-1] != "\"":
#             find_error.add(3)
#             pass
#         else:
#             pass
#
#         return find_error
#
#
#
