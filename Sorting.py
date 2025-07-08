#Bubble Sort
# def bubbleSort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]<arr[j+1]:
#             #swap
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# arr=[4,3,5,1]
# print(bubbleSort(arr))

# def bubSort(arr,ascending=True):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if (ascending and arr[j]>arr[j+1]) or (not ascending and arr[j]<arr[j+1]):
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# arr = [3,6,2,7,34,45,78]
# t=4
# f = arr[t:]
# s = arr[:t]
# print(bubSort(f)+bubSort(s))

#Selection sort
# def selectionSort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_i=i
#         for j in range(i+1,n):
#             if arr[j]>arr[min_i]:
#                 min_i = j
#             arr[j],arr[min_i]=arr[min_i],arr[j]
#     return arr
# arr=[64, 25, 12, 22, 11]
# print(selectionSort(arr))

#Quick Sort nlogn
# def QuickSort(arr):
#     if len(arr)<=1:
#         return arr
#     else: 
#         pivot=arr[0]
#         left=[x for x in arr[1:] if x<pivot]
#         right=[x for x in arr[1:] if x>=pivot]
#     return QuickSort(left) + [pivot] + QuickSort(right)

# arr=[34,67,12,-1,6,45,90]
# print(QuickSort(arr))


#Merge Sort
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    s_arr=[]
    i,j=0,0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            s_arr.append(left[i])
            i+=1
        else:
            s_arr.append(right[j])
            j+=1
    s_arr.extend(left[i:])
    s_arr.extend(right[j:])
    return s_arr

arr1 = [45, 8, 1, 3, 100, 11, 15]
s_arr = mergeSort(arr1)
print("Sorted Array:", s_arr)