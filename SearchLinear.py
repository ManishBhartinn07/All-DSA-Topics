def ls(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
arr=[3,2,5,9,2]
t = 9
print(ls(arr,t))