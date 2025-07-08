# def min_heap(arr,n,i):
#     smallest = i
#     left = 2*i+1
#     right = 2*i+2
#     # print(smallest,end=" ")
#     # print(left,end=" ")
#     # print(right,end=" ")
#     if left<n and arr[left]<arr[smallest]:
#         smallest = left
#     if right<n and arr[right]<arr[smallest]:
#         smallest=right

#     if smallest!=i:
#         arr[i],arr[smallest] = arr[smallest],arr[i]
#         min_heap(arr,n,smallest)
# def build_heap(arr,n):
#     for i in range(n//2-1,-1,-1):
#         min_heap(arr,n,i)

def max_heap(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[left] > arr[largest]:
        largest = left
    if right<n and arr[right] > arr[largest]:
        largest = right
    
    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heap(arr,n,i)
def build_heap(arr,n):
    for i in range(n//2-1,-1,-1):
        max_heap(arr,n,i)
def insert(heap,key):
    heap.append(key)
    i=len(heap)-1
    while i>0 and heap[(i-1)//2] < heap[i]:
        heap[i],heap[i-1//2] = heap[i-1//2],heap[i]
        i=i-1//2 
arr=[4,2,6,8,45,23]
n=len(arr)
insert(heap,18)
build_heap(arr,n)
print(arr)