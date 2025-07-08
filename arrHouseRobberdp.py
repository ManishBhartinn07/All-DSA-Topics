'''nums =
[200,3,140,20,10]

Use Testcase
Output
350
'''
# def robber(nums):
#     n=len(nums)
#     if n==0:
#         return 0
#     rob,norob=0,0
#     for num in nums:
#         newrob = num + norob
#         newnorob = max(rob,norob)
#         rob, norob = newrob, newnorob
#     return max(rob,norob)
# nums =[200,3,140,20,10]
# print(robber(nums))

'''nums =
[200,3,140,20,10]

Use Testcase
Output
340
Rob in alternate house and houses are in circle
'''

def robbing(nums):
    n=len(nums)
    if n==0:
        return 0
    
    dp = [0] *n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1], nums[i] + dp[i-2])
    return dp[-1]

