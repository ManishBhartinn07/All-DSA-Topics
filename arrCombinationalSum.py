
# def combinationSum(candidates, target):
#     def backtrack(start, target, path):
#         if target == 0:
#             result.append(path)
#             return
#         if target < 0:
#             return
#         for i in range(start, len(candidates)):
#             backtrack(i, target - candidates[i], path + [candidates[i]])

#     result = []
#     candidates.sort()
#     backtrack(0, target, [])
#     return result

# arr = [2,3,6,7]
# print(combinationSum(arr,7))

#Backtrack

def CombSum(arr,target):
    res = []
    n=len(arr)
    def dfs(i,curr,total):
        if total == target:
            res.append(curr.copy()) #we might use curr later for storing another sum
            return #Break
        if i>=n or total > target:
            return
        curr.append(arr[i]) #add all elements of array

        dfs(i,curr,total+arr[i]) # total on left side 
        curr.pop() #pop because on right we do not use same element
        dfs(i+1,curr,total) #on right
    dfs(0,[],0)
    return res
arr = [2,3,5]
print(CombSum(arr,8))