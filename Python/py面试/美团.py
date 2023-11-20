
# while 1:
#     nums=[]
#     s = input()
#     if s != "":
#         for x in s.split():
#             nums.append(int(x))
#     else:
#         break
# print(n,nums)
# sub = float('inf')
# for i in range(int(n)-1):
#     route_mei = nums[i]-nums[0]
#     route_tuan = nums[n-1]-nums[i]
#     sub = min(sub, abs(route_mei-route_tuan))
# print(sub)
# n = int(input())
# nums=[]
# s = input()
# if s != "":
#     for x in s.split():
#         nums.append(int(x))
# sub = float('inf')
# for i in range(n):
#     route_mei = nums[i]-nums[0]
#     route_tuan = nums[n-1]-nums[i]
#     sub = min(sub, abs(route_mei-route_tuan))
# print(sub)
# n = int(input())
# nums=[]
# s = input()
# if s != "":
#     for x in s.split():
#         nums.append(int(x))
# # window = 1
# r = 0
# sum = 0
# while window <= n:
#     for i in range(n-r*2):
#         nums_1 = sorted(nums[i:i+window])
#         sum += nums_1[r]
#         print(sum)
#         # if i+window == n -1:
#         #     break
#     r += 1
#     window = 2*r +1
# s = input()
# num = len(s)
# if num < 6:
#    print(0)
# sum_a = 0
# sum_b = 0
# sum_c = 0
# sum = 0
# for i in range(num):
#     if s[i] == 'a':
#         sum_a += 1
#     if s[i] == 'b':
#         sum_b += 1
#     if s[i] == 'c':
#         sum_c += 1
# sum = sum_c // 3
# if (sum_b >= sum and sum_a >= sum + 1):
#     print(sum)
n = int(input())
course = [0 for i in range(n)]
s = input()
for i in range(n):
    if s != "":
        t = 0
    for x in s.split():
        course[i]= str(course[i])+x
        t += 1
        if int(course[i][1]) == 0 or int(course[i][1]) + 1 == t:
            break
print(course)