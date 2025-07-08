# n = int(input("Enter a number: "))
# if(n%2 == 0):
#     print("Even")
# else:
#     print("Odd")

# import sys
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# sum = a+b
# print("Sum is: ",sum)

# n = input("Enter numbers in list : ").split()
# n = [int(x) for x in n]
# print("List of numbers:", n)
# sum = 0
# for x in n:
#     sum = sum + x
# print("Sum of numbers: ", sum)

# print("average of numbers : ",int(sum/len(n)))

# s1 = input("Enter a string: ")
# s2 = input("Enter string to concatinate: ")
# def reverse_string(s):
# 	return s[::-1]

# rev_str = reverse_string(s1)
# def conc_str(s1,s2):
# 	return (s1+s2)

# conc_str = conc_str(s1,s2)

# def find_substr(s1,s2):
# 	return s1.find(s2)

# print("Revesed string: ",rev_str)
# print("Concatinate: ",conc_str)
# print("Finding substring: ",find_substr(s1,s2))

#Max of 3 numbers define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
# def max_of_three(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# a = int(input("Enter first number: "))  
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print("Max of three numbers: ",max_of_three(a,b,c))

#Implement a python script for factorial of number by using recursion

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# n = int(input("Enter a number: "))
# print("Factorial : ",factorial(n))

#With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half 
#values in one line and the last half values in one line. 

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# l = len(t)
# print("First half values: ",t[:l//2])
# print("Second half values: ",t[l//2:])


#Write Python script to display file contents. 
# f = open("h.txt","r")

# print(f.read())
# f.close()

#Implement a python script to check the element is in the list or not by using Linear 
#search & Binary search 
# def linear_search(l,n):
#     for i in range(len(l)):
#         if l[i] == n:
#             return i
#     return -1

# def binary_search(l,n):
#     l.sort()
#     low = 0
#     high = len(l)-1
#     mid = 0
#     while low<=high:
#         mid = (low+high)//2
#         if l[mid]<n:
#             low = mid+1
#         elif l[mid]>n:
#             high = mid-1
#         else:
#             return mid
#     return -1

# l = [1,2,3,4,5,6,7,8,9,10]
# n = int(input("Enter a number: "))
# print("Linear search: ",linear_search(l,n))
# print("Binary search: ",binary_search(l,n))

#Write a program that repeatedly asks the user to enter product names and prices. Store 
#all of them in a dictionary whose keys are product names and values are prices. And 
#also write a code to search an item from the dictionary. 

# dic = {}
# n = int(input("Enter number of products: "))
# for i in range(n):
#     product = input("Enter product name: ")
#     price = int(input("Enter price: "))
#     dic[product] = price
# print(dic)
# search = input("Enter product to search: ")
# if search in dic:
#     print("Product found")
#     print("Price of ",search," is: ",dic[search])
# else:
#     print("Product not found")

#Write a python program to read data from a CSV file and print the contents.

# import pandas as pd # type: ignore
# data=pd.read_csv("ibm.csv")
# print(data)

# def longestSubString(s):
#     char_set=set()
#     left = 0
#     max_length = 0
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_length=max(max_length,right-left+1)
#     return max_length

# s=input()
# i=longestSubString(s)
# print(i)

# n="1337c0d3"
# a="0123456789"
# if len(n)>len
# for i in range(len(a)):
#     if n[i]!=a[i]:
#         b=n[i]
# print(b)

# a=[1,2,3,4,5]
# print(a[1])
# a=sorted(a)
# print(a[len(a)-2])

#Convert roman into 

# list1 = [1,2,3]
# list2 = [1,4,5]
# merged_list = sorted(list1+list2)
# print(merged_list)

# def mul(a):
#     return a*10
# print(mul(10))

# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))

# class chair:
#     def __init__(self,shape,colour):
#         self.shape = shape
#         self.colour = colour
#     def display(self):
#         print("f")

# v=chair("Vertical","Red")
# print(v.shape)

# a=[10,11,2,1,30]

# i=0
# for i in range(len(a)):
#     for j in range(0,len(a)-i-1): #first , last
#         if a[j]<a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a[1])


# b=a.sort()
# print(a[3])


# n=[3,2,4,1,7,6,5]
# # n.reverse()
# j=len(n)-1
# i=0
# while i<j:
#     n[i],n[j]=n[j],n[i]
#     j-=1
#     i+=1
# print(n)

# def odd_even(arr):
#     odd = 0
#     ev = 1

#     while odd<len(arr) and ev<len(arr):
#         if arr[ev]%2==0:
#             v=ev
#         if arr[odd]%2==0:
#             d=odd
#         odd+=2
#         ev+=2
#     arr[v],arr[d]=arr[d],arr[v]
#     return arr
# print(odd_even([1,2,3,4,6,8,9]))

# arr = [1,2,4,5,6,7]
# i=0
# j=len(arr)-1
# tar=11
# while i<j:
#     if arr[i]+arr[j]==tar:
#         # print(arr[i])
#         print(arr[i],arr[j])
#         i+=1
#         j-=1
#     elif arr[i]+arr[j]<tar:
#         i+=1
#     else:   
#         j-=1

# arr = [1,2,4,5,6,7]
# i=0
# j=len(arr)-1
# tar=3
# while i<j:
#     d=arr[j]-arr[i]
#     if d==tar:
#         print(arr[i],arr[j])
#         i+=1
#         j-=1
#     elif d>tar:
#         j-=1
#     else:   
#         i+=1

# arr = [1, 2, 4, 5, 6, 7]
# i = 0
# j = len(arr) - 1
# tar = 3

# while i < j:
#     d = arr[j] - arr[i]
#     if d == tar:
#         print(f"Pair found: {arr[i]}, {arr[j]}")
#         j -= 1 
#     elif d > tar:
#         j -= 1
#     else:
#         i += 1 
#     if j <= i:
#         i += 1
#         j = len(arr) - 1


# list=[1,2,3,4,5]
# for i,val in enumerate(list):
#     index=i+2
#     print(list[index])
#     break

# n=[1,2,2,1]
# i=0
# for i in range(0, len(n) - 1, 2):
#     if n[i] < n[i + 1]:
#         n[i], n[i + 1] = n[i + 1], n[i]
    
# print(n)

# n=[3,2,5,1,10,3]
# i=0
# for i in range(len(n)-1):
#     i=i%2
#     if i==0:
#         if n[i] < n[i+1]:
#             n[i], n[i+1] = n[i+1],n[i]
#     # else:
#     #     if n[i] > n[i+1]:
#     #         n[i],n[i+1] = n[i+1], n[i]
# # n.reverse()

# print(n[::-1])


# n = [1, 2, 3]
# result = sum_of_subarrays(n)
# print(result)

# def rd(arr):
#     arr1=sorted(arr)
#     uniq = []
#     for i in arr1:
#         if i not in uniq:
#             uniq.append(i)
#     print(uniq)
# arr = [4,2,3,1,1]
# rd(arr)

# def rm(nums,val):
#     return [x for x in nums if x != val]
# n=[3,4,5,3]
# val=3
# rm(n,val)
# print(n)

# s=[1,2,3,4]
# print(s[2:7])

# def sum_of_subarrays(arr):
#     total_sum = 0
#     n = len(arr)
    
#     for i in range(n):
#         for j in range(i, n):
#             subarray_sum = sum(arr[i:j+1])
#             total_sum += subarray_sum
    
#     return total_sum

# def sub(arr):
#     total_sum=0
#     n=len(arr)

#     for  i in range(n):
#         for j in range(i,n):
#             sub_sum=sum(arr[i:j+1])
#             total_sum+=sub_sum
#     print(total_sum)

# arr=list(map(int, input().split()))
# sub(arr)

# a=[1,2,3]
# def sub(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i,n):
#             print(arr[i:j+1])

# sub(a)

# def max_ssum(arr):
#     max_sum=float('-inf')
#     c_sum=0         
#     for num in arr:
#         c_sum=max(num, c_sum + num) 
#         max_sum=max(max_sum, c_sum)  
#     return max_sum
# arr=list(map(int, input().split()))
# sum = max_ssum(arr)
# print(sum)

# def max_sum(arr):
#     s = 0
#     arr.sort()
#     n=len(arr)
#     for i in range(n):
#         if arr[i]<0:
#             break
#         s=s+arr[i]
#     return s
# arr = [1,2,3,-1,0]
# max_sum(arr)


# def max_sum(arr):
#     s = 0
#     arr.sort()
#     n = len(arr)
#     for i in range(n):
#         if arr[i] < 0:  # Stop the loop if a negative element is encountered
#             break
#         s += arr[i]
#     return s

# arr = [1, 2, 3, -1, 0]
# print(f"Max sum: {max_sum(arr)}")  # Output: Max sum: 6


# def max_sum(arr):
#     s = 0
#     arr.sort(reverse=True)
#     for num in arr:
#         if num < 0:
#             break
#         s += num
#     return s
# arr = list(map(int, input().split()))
# print(max_sum(arr)) 

# def mamidiff(temp):
#     min=temp[0]
#     max=temp[0]
#     for i in temp:
#         if i>max:
#             max=i
#         if i<min:
#             min=i
#     return max-min
# def sub(a,m):
#     v=float('inf')
#     for i in range(len(a)-m):
#         temp=a[i:m+i]
#         t=mamidiff(temp)
#         if t<v:
#             v=t
#     return v
# print(sub([7, 3, 2, 4, 9, 12, 56],5))

# import string   
# a="abcD"
# n=len(a)
# end = ord(a[-1]) + 2
# for i in range(ord(a[2]),ord(end)):
#     print(chr(i))


# a = "abcd"
# n = len(a)
# start = ord(a[2])
# end = ord(a[-1]) + 2
# print(a[start:end])
# for i in range(start, end):
#     print(chr(i))

# for i in range(1,4):
#     v=chr(ord(i)+2)
#     print(v)

# nums=[1,2,3,3,2]
# val=3
# nums=[x for x in nums if x != val]
# print(nums)

# a=[1,2,3,4,5]
# print(a[1])
# a=sorted(a)
# print(a[len(a)-2])

# def max_of_three(a,b,c):
#     if a>b and a>c:
#         return a

#     elif b>a and b>c:
#         return b
#     else:
#         return

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print("Max of three numbers: ",max_of_three(a,b,c))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# n = int(input("Enter a number: "))
# print("Factorial : ",factorial(n))

# a=[4,8,2,3,8,1]
# def sec(a):
#     n=len(a)
#     a.sort()
#     for i in range(n-2,-1,-1):
#         if a[i]!=a[n-1]:
#             return a[i]

#     return -1
# sec(a)
# print(sec(a))
  
#input = [1,2,3]
#output = 1+2+1 =4  2-1 = 1, 3-2 = 1, 3-1=2
# arr = [1, 2, 3]
# sum = 0
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         sum += arr[j] - arr[i]  
# print(sum)



# arr = [1, 2, 3]
# result = 0

# for i in range(len(arr)):
#     for j in range(i):
#         result += abs(arr[i] - arr[j])

# print(result)

# def min(arr):
#     v=0
#     for i in arr:
#         if i>v:
#             v=i
#         else:
#             pass
#     print(v)
# def min(arr):
#     v=arr[0]
#     for i in arr:
#         if i<v:
#             v=i
#         else:
#             pass
#     print(v)
# arr=[20,3,54,21,100]
# min(arr)
# max(arr)

#area of container
# def area(h):
#     l=0
#     r=len(h)-1
#     area=0
#     while l<r:
#         c=min(h[l],h[r]) * (r-l)
#         area=max(area,c)
#         if h[l]<h[r]: l+=1
#         else: 
#              r-=1
#     return area   
# h=[9,1,2,3,4,5,8,2] 
# print(area(h))


# a=int(input())
# def happy_num(a):
#     seen=set()
#     while a!=1 and a not in seen:
#         seen.add(a)
#         a=sum(int(d)**2 for d in str(a))
#     return a==1
# print(happy_num(a))

# a=[1,2,3,1,2,3]
# k=3
# def dup(a,k):
#     s={}
#     for i,values in enumerate(a):
#         if values in s and i-s[values]<=k:
#             return True
#         s[values]=i
#     return False
# print(dup(a,k))

# print(a)
# a-- a[i]+1 == i


# a = [2, 3, 1, 6, 4,5]

# def consc(a):
#     m=1
#     l=1
#     a.sort()
#     for i in range(len(a)):
#         if a[i]==a[i-1]+1:
#             l+=1
#         elif a[i-1]+1 != a[i]:
#             m=max(m,l)
#             l=1
#     return max(m,l)

# print(consc(a))

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]

#Continuous Sum from start index to end index 
#[1,2,3,7,5] 12
#[2,4]

# def chori(arr):
#         # if i%2!=0:
#         #     c+=0
#         # else:
#     rob,norob=0,0
#     for num in arr:
#         newr = norob + num      #  0+2
#         newnrob = max(norob, rob) #max 0,0
#         rob,norob=newr,newnrob
#     return max(rob,norob)
# arr = [2,3,2]
# print(chori(arr))


# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
        
#         rob, norob = 0, 0
#         for num in nums:
#             newrob = num + norob
#             newnorob = max(rob, norob)
#             rob, norob = newrob, newnorob
        
#         return max(rob, norob)

# # Test Case
# nums = [200, 3, 140, 20, 10]
# sol = Solution()
# print(sol.rob(nums))  # Expected Output: 340


# arr=[0,1,2,3,4]
# for i in range(0,len(arr)):
#     if i != arr[i]:
#         print(i ,"is missing")
        
# print(n+1)

# arr=[1,1,1,3,3,4,3,2,4,2]
# arr.sort()
# for i in range(0,len(arr)-1):
#     if arr[i]==arr[i+1]:
#         print("True")
#         break
# print(False)

# n = 8
# x = 1  # person 2 (0-based index)
# moves = 3

# dp = [[0 for _ in range(n)] for _ in range(moves + 1)]
# dp[0][x] = 1

# for step in range(1, moves + 1):
#     for pos in range(n):
#         left = (pos - 1 + n) % n
#         right = (pos + 1) % n
#         dp[step][pos] = dp[step - 1][left] + dp[step - 1][right]

# print(f"Number of ways: {dp[moves][x]}")

arr= [12,5,7,23]

# j=1
# g=False
# for i in range(len(arr)-1):
#     if arr[i]<arr[j]:
#         g=True
#     j+=1
# print(g)


# nums=[2,4,2,2,5,2]

# k=2

# nums.sort()
# print(nums)
# t=[]
# for i in range(1,len(nums)):
#     if nums[i-1]-nums[i]<=k:
#         t.append(True)
#     else:
#         t.append(False)

# print(t)
# n=int(len(nums)/3)
# nums2=[[] for _ in range(n)]

# nums2=[nums[i:i +n] for i in range(0, len(nums), n)]

# print([] if False in t else nums2)
# # nums2[0].extend(nums[0:3])
# # nums2[1].append([4,5,6])
# # nums2[2].append([7,8,9])
# # print(nums2)

# def reverseVowels(s):
#     l = ['a','e','i','o','u']
#     s=s.lower()
#     s = list(s)
#     j = len(s)-1
#     i = 0
#     while i<j:
#         if s[i] in l and s[j] in l:
#             s[i],s[j] = s[j],s[i] 
#             i+=1 
#             j-=1
#         if s[i] in l:
#             j-=1
#         if s[j] in l:
#             i+=1
#     return ''.join(s)
# s = "IceCreAm"
# print(reverseVowels(s))

# s = "IceCreAm"
# s=s.lower()
# s=list(s)
# print(s)
# print(''.join(s))

# def vowelR(s):
#     t=("aeiouAEIOU")
#     s2=""
#     i=0
#     j=len(s)-1
#     s=list(s)
#     while i<j:
#         if s[i] in t and s[j] in t:
#             s[i], s[j] = s[j], s[i]
#             i+=1
#             j-=1
#         elif s[j] not in t:
#             j-=1
#         elif s[i] not in t:
#             i+=1
#     return ''.join(s)
# s="IceCream"
# print(vowelR(s))

# t=("aeiouAEIOU")
# print(t[1])

# from collections import Counter 

# a=[1,1,2,2,1,7,5]
# count=Counter(a)
# max_freq = max(count.values())
# max_f = [k for k,v in count.items() if max_freq==v]
# print(max_f)

# c=0
# t=0
# for i in range(len(a)):
#     c+=1
#     if t==max_freq:
#         t+=1
#         break
# print(c)


# arr=[2,2,2,2,2]
# key=2
# k=2
# res=[]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if abs(i-j)<=k and arr[j]==key:
#             res.append(i)
# print(list(set(res)))

# from collections import Counter
# a = "foo"
# t = "bar"
# c=[]
# d=[]
# for char in a:
#     c.append(a.count(char))
# for char in t:
#     d.append(t.count(char))

# c=list(set(c))
# d=list(set(d))
# print(c,d)
# for i in range(0,max(len(c),len(d))):
#     for j in range(0,min(len(d),len(c))):
#         if d[i] == c[i]:
#             print(False)
# print(True)

# def sec(nums1,nums2):
#     res = []
#     # for i in range(len(nums1)):
#     #     for j in range(len(nums2)):
#     #         m=min(nums1[i]*nums2[j],res[0])
#     #         res.append(m)
#     # res.sort()
#     print(res)
#     return res[k-1]

# print(sec(nums1,nums2))
nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3
# nums1 = [-4,-2,0,3]
# nums2 = [2,4]
# k = 6
# res=[]
# n1,n2=[],[]
# n1.extend(nums1[:2]+nums1[-2:])
# n2.extend(nums2[:2]+nums2[-2:])
# print(n1)
# print(n2)
# for i in range(len(n1)):
#     for j in range(len(n2)):
#         res.append(n1[i]*n2[j])
#         print(n1[i],n2[j])
# res.sort()
# print(res)
# print(res[k-1])
# # print(nums1[-2:])

# a="anagram"
# t = "nagaram"
# # rev=""
# # for char in a:
# #     rev = char + rev
# # print(rev)
# # print(rev == t)
# print(sorted(a)==sorted(t))
# s = "abcd"
# t = "abcde"

# for char in t:
#     if s.find(char)>=0:
#         print('')
#     else:
#         print(char)

# s = "1001010"
# k = 5

# binary no <= k

# words = 
# print(res)



# ["Hello","Alaska","Dad","Peace"]
# s1 = set("qwertyuiop")
# s2 = set("asdfghjkl")
# s3 = set("zxcvbnm")
# res = []
# for word in words:
#     l=set(word.lower())
#     if l.issubset(s1) or l.issubset(s2) or l.issubset(s3):
#         res.append(word)


nums = [0,10]
k = 2
# -2,-1,0,1,2
for i in range(len(nums)):
    # if i<len(nums) and i >= 0:
    nums[0] += k
    nums[1] -= k
        # nums[i] = nums[i]+2
print(max(nums)-min(nums))

    