#target sum using two pointers
# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 return True
#     return False
# arr=[1,2,3,-4,-1,5]
# target = 4
# print(two_sum(arr,target))

# def two_sum(arr,t):
#     arr.sort()
#     l=0
#     r=len(arr)-1
#     while l<r:
#         sum=arr[l]+arr[r]
#         if sum==t:
#             return True
#         elif sum<t:
#             l+=1
#         else:
#             r-=1
#     return False
# arr=[1,2,3,-4,-1,5]
# t=10
# print(two_sum(arr,t))

