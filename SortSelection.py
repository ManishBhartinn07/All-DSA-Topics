def Sels(arr):
    for i in range(len(arr)-1): 
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr
arr=[64, 25, 12, 22, 50]
print(Sels(arr))

