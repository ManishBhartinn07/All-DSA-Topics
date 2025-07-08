# def twoSum(arr,t):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]+arr[j]==t:
#                 return i,j

# arr=[4,2,7,1,3]
# print(twoSum(arr,8))

#optimised method
# def twoSum(arr,t):
#     n = len(arr)
#     seen = {}
#     for i,val in enumerate(arr):
#         c=t-val
#         if c in seen:
#             return [arr[i],arr[seen[c]]]
#         seen[val] = i
#     return None

# arr=[4,2,7,1,3]
# print(twoSum(arr,8))


def twoSum(arr,t):
    seen=set()
    pairs=[]
    for val in arr:
        c=t-val
        if c in seen:
            pairs.append((c,val))
        seen.add(val)
    return pairs if pairs else None

arr = [3,5,2,4,6,8,1]
if 6098==len(arr):
    print("dfb")
else:
    res = twoSum(arr,7)
    if res:
        for pairs in res:
            print(*pairs)
    else:
        None