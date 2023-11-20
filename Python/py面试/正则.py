# import re
# s = 'aaaaaaab'
# p = 'a*'
# print(re.match(p,s))

# strs=['ab','9c','abacd']
# class Solution:
#     def longestCommonPrefix(strs) -> str:
#         if not strs: return ""
#         str0 = min(strs)
#         print(str0)
#         str1 = max(strs)
#         print(str1)
#         for i in range(len(str0)):
#             if str0[i] != str1[i]:
#                 return str0[:i]
#         return str0
# print(Solution.longestCommonPrefix(strs))
#
# class Solution:
#     def removeElement(nums, val: int) -> int:
#         num = nums.count(val)
#
#         print(num)
#         for i in range(num):
#             nums.remove(val)
#             i += 1
#         print(nums)
#         return len(nums)
# print(Solution.removeElement([3,2,2,3],3))
# class Solution:
#     def removeDuplicates(nums) -> int:
#         for i in range(len(nums)):
#             num = nums.count(nums[i])
#             target = nums[i]
#             while num - 1 > 0:
#                 print('test')
#             i+=1
#         return len(nums)
# print(Solution.removeDuplicates([1,1,2]))
# import re
#
#
# class Solution:
#     def winnerOfGame(colors: str) -> bool:
#         alice = 0
#         bob = 0
#         for i in range(len(colors)):
#             if colors[i:i + 3] == 'AAA':
#                 alice += 1
#             elif colors[i:i + 3] == 'BBB':
#                 bob += 1
#             i += 1
#             if i + 1 == len(colors) - 1:
#                 break
#         print(alice,bob)
#         if alice > bob:
#             return True
#         else:
#             return False
#
#
# Solution.winnerOfGame('AAAABBBB')
# class Solution:
#     def strStr(haystack: str, needle: str) -> int:
#         if haystack == '' and needle != '':
#             return -1
#         s = 0
#         for i in range(len(haystack) - len(needle) + 1):
#
#             if haystack[i:i + len(needle)] == needle:
#                 return i
#             i += 1
#             s += 1
#         print(s)
#         if s == len(haystack) - len(needle):
#             return -1
# print(Solution.strStr("aaaaa","bba"))
# print(min(6,7))
# num1='11'
# num2='123'
# num_1  = 0
# num_2 = 0
# print(num1[0],num1[1])
# for i in range(len(num1)):
#     num_1 += (10^(len(num1)-1-i))*int(num1[i])
#     i+=1
#     print(num_1)
# for i in range(len(num2)):
#     num_2 += (10^(len(num2)-1-i))*int(num2[i])
#     i+=1
#     print(num_2)
# print(str(num_1 + num_2))