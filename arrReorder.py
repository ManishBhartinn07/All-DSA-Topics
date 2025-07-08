def reOrder(arr,r):
    n=len(arr)
    t=n-r
    l=arr[0:t]
    r=arr[t:n]
    # print(r)
    # print(str(l))
    return r+l[::-1]
arr = list(map(int, input().split()))
r = int(input())
if len(arr)==0:
    print("ahebfws")
else:
    print(*reOrder(arr,r))
