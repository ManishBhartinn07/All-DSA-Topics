'''
Input: arr[] = [2, 4, 6, 8], target = 8
Output: [[2 2 2 2] [2 2 4] [2 6] [4 4] [8]]
Explanation: Total number of possible combinations are 5.
'''

def helper(arr,target,curr,index,res):
    if target==0:
        res.append(list(curr))
        return
    for i in range(index, len(arr)):
        if arr[i]>target:
            continue
        curr.append(arr[i])
        helper(arr,target-arr[i],curr,i,res)
        curr.pop()

def combSum(arr, target):
    arr.sort()
    res = []
    helper(arr,target,[],0,res)
    return res
arr = [1,2,3]
t = 4
res=combSum(arr,t)
print(res)
print(len(res))
