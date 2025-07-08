'''
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#basic approach
# def ClimbingS(n):
#     def climb(n):
#         if n==1:
#             return 1
#         if n==2:
#             return 2
#         return climb(n-1)+climb(n-2)
#     return climb(n)
# n=int(input())
# print(ClimbingS(n))

#using dp
def Climb(n):
    if n==1:
        return 1
    if n==2:
        return 2
    prev1,prev2 = 2,1
    for i in range(3,n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
n=int(input())
print(Climb(n))