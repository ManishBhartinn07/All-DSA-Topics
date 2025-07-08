def solve(arr, i, v, result):
    if i == len(arr):
        result.append(v[:])  # Store the subset
        return
        
    # Include the current element
    v.append(arr[i])
    solve(arr, i + 1, v, result)
        
    # Exclude the current element
    v.pop()
    solve(arr, i + 1, v, result)
    
def subsets(arr):
    result = []
    solve(arr, 0, [], result)
    # result.sort()
    return result
arr=[1,2,3]
print(subsets(arr))