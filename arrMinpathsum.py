'''
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
'''
# def minSum(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i):
#             sum+=arr[i][j]

# print(grid[0][1])
# for i in range(len(grid)):
#     for j in range(i):
#         sum +=grid[i][j]
# print(sum)
import math
grid = [[1,2,3],[4,5,6],[7,8,9]]
lc= sum(row[-1] for row in grid)
print(lc)
