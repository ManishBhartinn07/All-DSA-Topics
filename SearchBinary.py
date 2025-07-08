# Iterative Binary Search Algorithm:
# def Bs(arr,t,l,r):
#     while l<=r:
#         mid = l + (r-l) // 2
#         if arr[mid]==t:
#             return mid
#         elif arr[mid]<t:
#             l=mid+1
#         else:
#             r=mid-1
#     return -1
# arr = [1,2,3,4,5,6,7,9]
# t=0
# print(Bs(arr,t,0,len(arr)-1))

# Recursive Binary Search Algorithm:
def recB(arr,t,low,high):
    if low<=high:
        mid=low+(high-low)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            return recB(arr,t,low,mid-1)
        else:
            return recB(arr,t,mid+1,high)
    else:
        return -1
arr=[2, 3, 4, 10, 40]
t = 10
r = recB(arr,t,0,len(arr)-1)
if r==-1:
    print("Not Present")
else:
    print("Present at index : ",r)