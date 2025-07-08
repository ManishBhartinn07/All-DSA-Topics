#check max element
# import heapq
# max_heap=[]
# elements = [10,4,8,3,2,11,9]
# for num in elements:
#     heapq.heappush(max_heap,-num) #Storing in heap , default in top but in negative
# # max_ele = -heapq.heappop(max_heap)
# # smax_ele = -heapq.heappop(max_heap) #to get second max
# # print(max_ele)
# # print(smax_ele)
# # 
# # Get n max element 
# m=int(input())
# nmax_ele = 0
# for i in range(m):
#     nmax_ele = -heapq.heappop(max_heap)
# print(nmax_ele)

#Check min element
import heapq
min_heap=[]
arr=[10,4,8,3,2,11,9]
for num in arr:
    heapq.heappush(min_heap,num) #it stores elements in ascending order by default
n=int(input())
min_ele = 0
for i in range(n):
    min_ele = heapq.heappop(min_heap)
print(min_ele)
