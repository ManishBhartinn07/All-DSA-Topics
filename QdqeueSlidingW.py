#Fixed sized window 

# from collections import deque
# a=[1,3,-1,-3,5,3,6,7]
# k=3
# def maxSlidingW(a,k):
#     n=len(a)
#     result = []
#     dq = deque()
#     for i in range(n):
#         #left waale pop
#         if dq and dq[0]<i-k+1:
#             dq.popleft() 
#         #Agr window ke elements chote ho
#         while dq and a[dq[-1]] < a[i]:
#             dq.pop()
#         dq.append(i)

#         if i>=k-1: #ar koi window bni hogi
#             result.append(a[dq[0]])
#     return result

# print(maxSlidingW(a,k))

# from collections import deque
# def maxSum(a,s):
#     n=len(a)
#     res=float('-inf')
#     dq=deque()
#     w=0
#     if s<=0 and n==0:
#         return 0
#     for i in range(n):
#         w+=a[i]
#         if i>=s:
#             w-=a[i-s]
#         if i>=s-1:
#             res = max(res,w)
#     return res
# a=[1,2,6,-4,2,1]
# print(maxSum(a,3))

# def max_sum(a,s):
#     n=len(a)
#     w=0
#     res=float('-inf')
#     for i in range(n):
#         w+=a[i]
#         if i>=s:
#             w-=a[i-s]
#         if i>=s-1:
#             res = max(res,w)
#     return res
# a=[1,2,6,-4,2,1]
# print(max_sum(a,3))

'''
Variable Sized Window
'''
def max_w(arr):
    n=len(arr)
    sett=set()
    res=0
    l=0
    for r in range(n):
        while arr[r] in sett:
            sett.remove(arr[l])
            l+=1
        w=(r-l)+1
        res = max(res,w)
        sett.add(arr[r])
    return res
arr = "abcabcbb"
print(max_w(arr))
