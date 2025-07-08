def maxSub(arr):
    max_sum=float('-inf')
    curr_sum=0
    for num in arr:
        curr_sum=max(num,curr_sum+num)
        max_sum=max(curr_sum,max_sum)
    return max_sum
arr=list(map(int,input().split()))
print(maxSub(arr))
