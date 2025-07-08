# def duplicateNum(arr):
#     x1=0
#     n=len(arr)
#     for num in arr:
#         x1^=num
#     x2=0
#     for i in range(n):
#         x2^=i
#     return x1^x2

# print(duplicateNum(arr))


# arr=[1,2,2,3,3,4,4,4,4,4,4,5]
# # l=list(set(arr))
# # print(l)
# def dup(arr):
#     seen = set()
#     d = set()

#     for num in arr:
#         if num in seen:
#             d.add(num)
#         seen.add(num)
#     return list(d)

# print(dup(arr))

# from collections import Counter
# def findDup(arr):
#     f=Counter(arr)
#     d=[]
#     for key,value in f.items():
#         if value>1:
#             d.append(key)
#             continue
#     # d=[key for key,value in f.items() if value > 1 continue]
#     return d
# arr=[1,2,2,3,4,5,9,2]
# print(findDup(arr))