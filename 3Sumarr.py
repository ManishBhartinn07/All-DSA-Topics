# def threeSum(arr,t):
#     res = set()
#     arr.sort()
#     print(arr)
#     n=len(arr)
#     for i in range(n-2):
#         seen = set()
#         for j in range(i+1,n):
#             c = t - (arr[i]+arr[j])
#             if c in seen:
#                 res.add((arr[i],c,arr[j]))
#             seen.add(arr[j])
#     return [list(trip) for trip in res]
# arr = list(map(int,input().split()))
# print(threeSum(arr,0))


def tSum(arr,t):
    arr.sort()
    res = []
    n=len(arr)
    for i in range(n-2):
        seen = set()
        for j in range(i+1,n):
            c=t-(arr[i]+arr[j])
            if c in seen:
                res.append((arr[i],c,arr[j]))
            seen.add(arr[j])
    res = sorted(set(res))
    # for trp in res:
    print(res)
arr = [3,1,6,3,8,5,6,0,1]
tSum(arr,7)

