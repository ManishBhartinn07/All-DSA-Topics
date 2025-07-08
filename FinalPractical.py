# Q.1
#744
# Find Smallest Letter Greater Than Target
'''Input:letters = ["c","f","j"], 
target = "a"
Output: "c"

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
'''
# def nextGL(l,t):
#     t=ord(t)-ord('a') //97 - 97 = 0
#     for i in l:
#         lo=ord(i)-ord('a') //99 - 97 = 2 
#         if lo>t: #2>0
#             return i
#     return l[0]
# l=["c","f","j"]
# t="a"
# print(nextGL(l,t))

# Q.2
#475
#Heaters
# def findRadius(houses, heaters):
#     l = 0
#     r = 1e9
#     n = len(houses)
#     m = len(heaters)
#     houses.sort()
#     heaters.sort()
#     def checkHeat(mid: int):
#         fst = 0
#         snd = 0
#         while fst < n and snd < m:
#             while fst < n and \
#             heaters[snd]+mid >= houses[fst] and heaters[snd]-mid <= houses[fst]:
#                 fst+=1
#             snd+=1
#         return (fst >= n)

#     while l < r:
#         mid = int((l+r)//2)
#         if not checkHeat(mid):
#             l = mid + 1
#         else:
#             r = mid
        
#     return l
# h=[1,2,3,4]
# heaters=[1,4]
# print(findRadius(h,heaters))

# Q.9
#71
#Simplify path
# Input: path = "/home//foo/"
# Output: "/home/foo"
# path="/home/"
# def sp(p):
#     components = path.split("/")
#     s=[]
#     for comp in components:
#         if comp == "" or comp == ".":
#             continue
#         if comp == "..":
#             if s:
#                 s.pop()
#         else:
#             s.append(comp)
#     return "/" + "/".join(s)
# print(sp(path))

# Q.8
# 268. 
# Missing Number

# nums = [3,0,1]
# def missingNumber(a):
#     a.sort()
#     for i in range(0,len(a)):
#         if i!=a[i]:
#             return i
#     return len(a)
# print(missingNumber(nums))

# Q.3
# 506
# Relative Ranks
# score = [10,3,8,9,4]
# def RR(score):
#     score_map={score[i]: i for i in range(len(score))}
#     score.sort(reverse=True)
#     print(score)
#     l=["" for _ in range(len(score))]  
#     for i in range(len(score)):
#         if i==0:
#             l[score_map[score[i]]]="First"
#         elif i==1:
#             l[score_map[score[i]]]="Second"
#         elif i==2:
#             l[score_map[score[i]]]="Third"
#         else:
#             l[score_map[score[i]]]=str(i+1)
#     return l
# print(RR(score))
# print(score)


# Q.4
# 378. 
# Kth Smallest Element in a Sorted Matrix
# matrix = [[1,5,9],[10,11,13],[12,13,15]]
# k = 8

# def kthSmallest(m,k):
#     l=[]
#     for i in range(len(m)):
#         l+=m[i]
#     l.sort()
#     return l[k-1]
# n=int(input())
# k=8
# matrix=[]
# for i in range(n):
#     r=list(map(int,input().split()))
#     matrix.append(r)
# print(kthSmallest(matrix,k))


# Q.5
#33
#Search in Rotated Sorted Array
# nums = [4,5,6,7,0,1,2]
# t = 0
# def Rsa(nums,t):
#     for i in range(len(nums)):
#         if t==nums[i]:
#             return i
#     return -1
# print(Rsa(nums,t))

# Q.6
# 455.
# Assign Cookies
# Input: g = [1,2,3], s = [1,1]
# Output: 1
# def fcc(g,s):
#     l=0
#     g.sort()
#     s.sort()
#     for cSize in s:
#         if cSize >= g[l]:
#             l+=1
#             if l==len(g): break
#     return l
# g=list(map(int,input().split()))
# s=list(map(int, input().split()))
# print(fcc(g,s))

# Q.7
# 9. 
# Palindrome Number
# x = 1223333221
# def isPalindrome(x):
#     return str(x) == str(x)[::-1]
# print(isPalindrome(x))


# Q.10
#53
# Maximum Subarray
# a=[-2,1,-3,4,-1,2,1,-5,4]
# def maxSum(a):
#     max_sum=float('-inf')
#     c_sum=0
#     for num in a:
#         c_sum+=num
#         if c_sum>max_sum:
#             max_sum=c_sum
#         if c_sum<0:
#             c_sum=0
#     return max_sum

# print(maxSum(a))