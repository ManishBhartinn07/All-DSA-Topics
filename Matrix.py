#Rotate 90 degree
# def rotate(m):
#     m.reverse()
#     print(m)
#     for i in range(len(m)):
#         for j in range(i):
#             m[i][j],m[j][i]=m[j][i],m[i][j]
#     return m
# m=[[1,2,3],[4,5,6],[7,8,9]]
# print(rotate(m))

# matrix = [[1,2],[1,3]]
# k = 2
# # matrix=[[-5]]

# print(len(matrix))
# print(matrix[1])
# l=[]
# for i in range(len(matrix)):
#     l+=matrix[i]
# print(l)
# print(l[k])

nums = [3,30,34,5,9]
m1,m2=0,0
s=0
for num in nums:
    if num>9:
        num=str(num)
        s=list(num)
        m1=max(m1,s)
    else:
        m2=max(m1, num)
print(m1,m2)