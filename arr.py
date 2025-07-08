
# arr=[1,2,3,4,5]
# print(arr)

# for i in range(len(arr)):
#     print(arr[i])

# n=int(input())
# arr = []
# for i in range(n):
#     ele = int(input())
#     arr.append(ele)

# print(arr) 

#take input in one line
# a=list(map(int,input().split(' ')))
# print(a)
# s=0
# for i in range(len(a)):
#     s=s+a[i]
#     i=i+1
# print(s)


# import numpy as np

# arr1=np.array(list(map(int,(input().split()))))
# print(arr1)


# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# merged_arr=sorted(arr1+arr2)
# print(merged_arr)
# b=len(merged_arr)
# d=b/2
# if (b%2==0):
#     c=b//2
#     print(f"{((merged_arr[c]+merged_arr[c-1])/2):.4f}")
# else:
#     c=(b)//2
#     print(merged_arr[c])


# s="hello"
# print(s[0:3])
# s1=s[::-1]
# print(s1)

#Palindrome
# s=int(input())
# t=str(s)
# rev_s=t[::-1]

# if rev_s == t:
#     print("P")
# else:
#     print("Not p")

# n=int(input())
# rev_num=0
# o=n
# while n>0:
#     d=n%10
#     rev_num=rev_num*10 + d
#     n=n//10

# print(rev_num)

# if rev_num==o:    print("P")
# else:
#     print("NP")

# def longest_palindromic_substring(s: str) -> str:
#     def is_palindrome(sub: str) -> bool:
#         return sub == sub[::-1]  # Check if the string is equal to its reverse

#     longest = ""
#     n = len(s)

#     for i in range(n):
#         for j in range(i, n):
#             substring = s[i:j + 1]  # Extract substring
#             if is_palindrome(substring) and len(substring) > len(longest):
#                 longest = substring  # Update if it's the longest palindrome

#     return longest

# s=input()

# l=longest_palindromic_substring(s)
# print(l)


# def rev(num):
#     rev = a[::-1]


# num = int(input())
# num = abs(num)
# a = str(num)
# rev = int(rev)

# def c_sum(arr,t):
#     start=0
#     n=len(arr)
#     c_sum=0
#     for end in range(n):
#         c_sum+=arr[end]
#         while c_sum>t and start<=end:
#             c_sum-=arr[start]
#             start+=1
#         if c_sum==t:
#             return [start+1,end+1]
# arr=[1,2,3,7,5]
# t=12
# print(c_sum(arr,t))

# Input: arr[] = [1, 2, 0, 3]
# Output: 2 
# Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3
# def eql(arr):
#     n=len(arr)
#     t_sum=sum(arr)
#     l_sum=0
#     for i in range(n):
#         r_sum = t_sum - l_sum - arr[i]
#         if r_sum == l_sum:
#             return i
#         l_sum += arr[i]
#     return -1
# arr=[1,2,0,3]
# print(eql(arr))

#Product Array Puzzle
# Input: arr[] = [10, 3, 5, 6, 2]
# Output: [180, 600, 360, 300, 900]

# def prodE(arr):
#     n=len(arr)
#     res = [1]*n
#     prefix=1
#     for i in range(n):
#         res[i] = prefix
#         prefix *= arr[i]
#     suffix=1
#     for i in range(n-1,-1,-1):
#         res[i] *= suffix
#         suffix *= arr[i]
#     return res

# arr=[10,3,5,6,2]
# print(prodE(arr))


# def duplicateNum(arr):
#     x1=0
#     n=len(arr)
#     for num in arr:
#         x1^=num
#     x2=0
#     for i in range(n):
#         x2^=i
#     return x1^x2

# print(duplicateNum(arr))


# arr=[1,2,2,3,3,4,4,4,4,4,4,5]
# # l=list(set(arr))
# # print(l)
# def dup(arr):
#     seen = set()
#     d = set()

#     for num in arr:
#         if num in seen:
#             d.add(num)
#         seen.add(num)
#     return list(d)

# print(dup(arr))

# arr = [1,-2,3,5,4,8,-3,-7]
# sum=0
# c=0
# for i in range(len(arr)):
#     if arr[i]>0:
#         sum+=arr[i]
#         c+=1
# print(sum)
# print(c)

# n=int(input())
# # arr = [int(input(f"Enter elements {i+1}: ")) for i in range(n)]
# arr=[int(input()) for i in range(n)]
# print(arr)

#increasing order

def inc(arr):
    n=len(arr)
    c=0
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            if c==1:
                return False
            c+=1
            if i==1 or arr[i-2] <= arr[i]:
                arr[i-1]=arr[i]
            else:
                arr[i]=arr[i-1]
    return True      
arr=[4,2,1]
print(inc(arr))