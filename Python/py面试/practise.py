# s = "pwwkew"
# num = len(s)
# Hashmap = set()
# window = 0
# L = 0
# for i in range(num):
#     window += 1
#     if s[i] in Hashmap:
#         # window -= 1
#         while s[i] in Hashmap:
#             Hashmap.remove(s[L])
#             window -= 1
#             L += 1
#         Hashmap.add(s[i])
#     else:
#         Hashmap.add(s[i])
#     print(window)
# print(window,Hashmap)
#
# nums = set()
# nums.add('a')
# nums.add('a')
# print(nums)
# s= "ccaab"
# window = 0
# Hashmap = dict()
# res = 0
# L = 0
# for i in s:
#     Hashmap.update('i')
#     window += 1
#     while len(Hashmap)>2:
#         Hashmap.remove(s[L])
#         L += 1
#         window -= 1
#         print(res, Hashmap)
#     if window>res:
#         res = window
#     print(window)
#
# nums = sorted(num_map, key=abs)
# print(nums)
# example_list = [5, 0, 6, 1, 2, 7, 3, 4]
# result_list = sorted(example_list, key=lambda x: x*-1)
# print(result_list)
import collections

# arr= [3,-1,-3,6]
# num_map = collections.Counter(arr)
# print(sorted(num_map, key=abs))
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# n = len(nums)
# q = collections.deque()
#
# for i in range(k):
#     while q and nums[i] >= nums[q[-1]]:
#         q.pop()
#     q.append(i)
# #
# print(q)
# ans = [nums[q[0]]]
# print(ans)
# for i in range(k, n):
#     while q and nums[i] >= nums[q[-1]]:
#         q.pop()
#     q.append(i)
#     print(q)
#     while q[0] <= i - k:
#         q.popleft()
#     print('弹栈',q)
#     ans.append(nums[q[0]])
# print(ans)
# # return ans
# t= "ABC"
# s= "ADOBECODEBANC"
# # Hashmap = collections.Counter(t)
# # substring = collections.defaultdict(int)
# # print(substring != Hashmap)
# need=collections.Counter(t)
# needCnt=len(t)
# i=0
# res=[0,len(s)+1]
# for j,c in enumerate(s):
#     print(s[i])
#     if need[c]>0:
#         needCnt-=1
#         need[c]-=1
#     if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
#         while True:      #步骤二：增加i，排除多余元素
#             c=s[i]
#             if need[c]==0:
#                 break
#             # need[c]+=1
#             i+=1
#         print(need)
#         if j-i<res[1]-res[0]:   #记录结果
#             res=[i,j]
#         need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
#         needCnt+=1
#         i+=1
# print(s[res[0]:res[1]+1])

nums= [2,3,1,2,4,3]
# num = len(nums)
# target = 7
# total = 0
# L = 0
# ans = len(nums) + 1
# for R in range(num):
#
#
#     total = sum(nums[L:R + 1])
#     if total >= target:
#         ans = min(ans, R-L+1)
#     # print(ans)
#     while total >= target:
#         L += 1
#         total = sum(nums[L:R + 1])
#     if R==num-1 and total<target:
#         ans = R-L+2
#     # if R == num-1:
#     #     ans = min(ans, R-L+1)
# print(ans)
# window = collections.deque()
# num  = collections.deque(nums)
# print(window, num)
# print(int('A'))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# head = [1,1,2]
# Hashmap = set()
# while head:
#     Hashmap.add(head.val)
#     head = head.next
# print(Hashmap)
# n = 1101
# res = 0
# for i in range(4):
#     print(bin(n & 1), bin(res << 1))
#     res = (res << 1) | (n & 1)
#     print(bin(res))
#     n >>= 1
# #     print(bin(n))
# # print(res)
# s='XXX'
# nums = []
# for i in s:
#     if i == 'I':
#         nums.append(1)
#     if i == 'V':
#         nums.append(5)
#     if i == 'x':
#         nums.append(10)
#     if i == 'L':
#         nums.append(50)
#     if i == 'C':
#         nums.append(100)
#     if i == 'D':
#         nums.append(500)
#     if i == 'M':
#         nums.append(1000)
# print(nums)
# nums = [1,2,2,3]
# a = sorted(nums)
# b = a
# b.reverse()
# print(a,b,nums)
# if a==nums or nums==b:
#     print('True')
# else:
#     print('False')
# text_source = "xb 1 cc 5 dd 10 ee 2"
# text_source = "  "
#
# data = text_source.split()
# num = []
# word = []
# for i in data:
#     if i.isalpha()==0:
#         num.append(int(i))
#     else:
#         word.append(i)
# num.sort()
# for i in num:
#     word.append(str(i))
# words = ' '.join(word)
# print(words)
# print(data)
# words = 'PascalCaseTest'
# data = []
# if '-' in words:
#     data = words.split('-')
# elif '_' in words:
#     data = words.split('-')
# else:
#     L = 0
#     for i in range(1,len(words)):
#         if words[i]<'a':
#             data.append(words[L:i])
#             L = i
#     data.append(words[L:])
# data.lower()
# type_1 = '_'.join(data)
# type_2 = '-'.join(data)
# for i in range(1,len(data)):
#     s=data[i]
#     s[0].upper()
#     data[i]=s
# type_3 = ''.join(data)
# s=data[0]
# s[0].upper()
# data[0]=s
# type_4 = ''.join(data)
# s = "egg"
# word_s = collections.Counter(s).values()
# s = list(word_s)
# print(s)
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# times1 = collections.Counter(nums1)
# times2 = collections.Counter(nums2)
# num = times1 & times2
# print(times2,times1,num)
# list(num.elements())
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix.pop(0))
# print(list(zip(*matrix))[::-1])
# matrix = list(zip(*matrix))[::-1]
# matrix.pop(0)
# print(list(zip(*matrix))[::-1])
# matrix = list(zip(*matrix))[::-1]
# matrix.pop(0)
# print(list(zip(*matrix))[::-1])
# import re
# words = '()'
# # s=re.sub(r'\((\**)\)', r'\1', words)
# s = re.sub(r'\((\**)\)', r'(\1)()', words,count=1)
# s1 = re.sub(r'\((\**)\)', r'((\1))', words,count=1)
#
# print(s,s1)
# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# m,n = len(obstacleGrid), len(obstacleGrid[0])
# dp = [[1 for i in range(n)]for i in range(m)]
# for i in range(m):
#     if i == 0:
#         continue
#     for j in range(n):
#         if j == 0:
#             continue
#         dp[i][j] = dp[i-1][j]+dp[i][j-1]
#         if obstacleGrid[i][j] == 0:
#             dp[i][j] = 0
# print(dp)
# nums = [-1,2,3]
# res = list(set(nums))
# res.sort()
#
#
# print(res)
# print(3%5)
# for i in range(26):
#     s = chr(i+65)
#     print(s)
# def maxConsecutiveChar(ch: str) -> int:
#     s = "ABAB"
#     ans, left, sum = 0, 0, 0
#     for right in range(len(s)):
#         sum += s[right] != ch
#         while sum > 2:
#             sum -= s[left] != ch
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
#
# res = 0
# for i in range(26):
#     s = chr(i + 65)
#     print(maxConsecutiveChar(s))
#     res = max(res, maxConsecutiveChar(s))
# print(res)
# class Solution:
#     def characterReplacement(s: str, k: int) -> int:
#         def maxConsecutiveChar(ch: str) -> int:
#             ans, left, sum = 0, 0, 0
#             for right in range(len(s)):
#                 sum += s[right] != ch
#                 while sum > k:
#                     sum -= s[left] != ch
#                     left += 1
#                 ans = max(ans, right - left + 1)
#             return ans
#
#         res = 0
#         for i in range(26):
#             s = chr(i + 65)
#
#             res = max(res, maxConsecutiveChar(s))
#         return res
# print(Solution.characterReplacement('ABAB',2))
# class Solution:
#     def checkPossibility(nums) -> bool:
#         for i in range(len(nums)):
#
#             old = nums
#             n = nums[i]
#             old.pop(i)
#             new = sorted(old)
#             print(new,old)
#             if new == old:
#                 return True
#             old.insert(i,n)
#         return False
# print(Solution.checkPossibility([2,3,3,2,4]))
# print(ord('1'))
# s = "abc"
# queue = collections.deque(s)
# print(queue)
# temp = collections.deque()
# res = []
# temp.append(1)
# while temp:
#     num = temp.popleft()
#     if num in res:
#         pass
#     else:
#         res.append(num)
#     temp.append(num*2)
#     temp.append(num*3)
#     temp.append(num*5)
#     if len(res) == 30:
#         break
# res.sort()
# print(res)
# print(ord('a'))
nums = [1,3,1,5,3,6,8,9,0,2,23,5,6]
# target = 3
# L,count = 0,0
# for R,x in enumerate(nums):
#     # while abs(x-nums[L]) <= target and L<R:
#     #     L += 1
#     #     count += 1
#     while abs(x-nums[L]) > target:
#         L += 1
#     count += R - L
# print(count)
# nums.sort()
# print(nums)
# def test(nums)->int:
#     word = collections.Counter(nums)
#     nums.sort()
#     ans = 0
#     for i in range(1,len(nums)):
#         if nums[i]-nums[i-1] == 1:
#             ans = max(ans, word[nums[i]] + word[nums[i-1]])
#     return ans

#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param s string字符串
# @return string字符串
#
# class Solution:
#     def longestPalindrome(s) :
#         # write code here
#         num = 0
#         res = ''
#         L,R = 0,len(s)-1
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 temp = s[i:j+1]
#                 temp1 = temp[::-1]
#
#                 # print(temp1)
#                 if temp == temp1:
#                     if len(temp) > num:
#                         num = len(temp)
#                         res = temp
#         return res
# print(Solution.longestPalindrome("babad"))
# class Solution:
#     def MergeAarryNum(nums1, m, nums2, n) :
#         # write code here
#         length = m + n - 1
#         while m > 0 and n > 0:
#             if nums1[m - 1] > nums2[n - 1]:
#                 nums1[length] = nums1[m - 1]
#                 m -= 1
#             else:
#                 nums1[length] = nums2[n - 1]
#                 n -= 1
#             length -= 1
#         nums1[:n] = nums2[:n]
#         return nums1
# print(Solution.MergeAarryNum([1,2,3,0,0,0],6,[4,5,6],3))
# nums = [0,0,0,0]
# nums[0] = round(74.4-nums[0],2)*10
# nums[1] = round(78-nums[1],2)*15
# nums[2] = round(80.2-nums[2],2)*20
# nums[3] = round(80.4-nums[3],2)*25
# print(nums)
# nums1 =[258.0, 363.0, 998.0, 1210.0]
# a = sum(nums)
# print(a)
nums = [7, 9, 8, 5, 2, 4, 3, 6, 1]
L = 0
R = 8
key = nums[L]
while L < R:
    while (L < R) & (nums[R] > key):
        R -= 1
    while (L < R) & (nums[L] <= key):
        L += 1
    if L<R:
        nums[L],nums[R]=nums[R],nums[L]
nums[0],nums[L]=nums[L],nums[0]
print(nums)
print(L)
print(R)

