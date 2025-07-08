# *
# **
# ***
# def star(n):
#     j=n
#     for i in range(1,n+1): 
#         print("*" * i)
# n=3
# star(n)

# ***
# **
# *
# def star(n):
#     i=n
#     while i>0:
#         print("*" * i)
#         i-=1
# star(3)

# def star(n):
#     i=n
#     while i>0:
#         print("*" * i)
#         i-=1
#     for i in range(1,n+1):
#         print("*"*i)
# star(4)


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# def ustar(n):
#     i=n
#     for i in range(1,n+1):
#         print("*"*i)
# def nstar(n):
#     i=n
#     while i>0:
#         print("*" * i)
#         i-=1

# def main(n):
#     ustar(n)
#     for i in range(n+1):
#         print("*",end="")
#     print("")
#     nstar(n)

# main(4)

#By recursion
# def star(n):
#     if n>0:
#         star(n-1)
#         print(n * "*")
# star(3)

#Snake Pattern
# mat = [[10, 20, 30, 40],
    #    [15, 25, 35, 45],
    #    [27, 29, 37, 48],
    #    [32, 33, 39, 50]]

# Output : 10 20 30 40 45 35 25 15 27 29
#          37 48 50 39 33 32 

# m=4
# n=4
# def snake(mat):
#     global m,n
#     for i in range(m):
#         if i%2==0:
#             for j in range(n):
#                 print(str(mat[i][j]),end=" ")
#         else:
#             # for j in range(n-1,-1,-1):
#             #     print(str(mat[i][j]),end=" ")
#             while j>=0:
#                 print(str(mat[i][j]),end=" ")
#                 j-=1
# mat = [[10, 20, 30, 40],
#        [15, 25, 35, 45],
#        [27, 29, 37, 48],
#        [32, 33, 39, 50]]
# snake(mat)

# Tower of Hanoi
# def TowerofH(n,from_r,to_r,aux_r):
#     if n==0:
#         return
#     TowerofH(n-1,from_r,aux_r,to_r)
#     print("Move disk ",n," From ",from_r," to ",to_r)
#     TowerofH(n-1,aux_r,to_r,from_r)
# TowerofH(3,'A','C','B')

#Factorial 5-1 n(n-1)
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return (n * fact(n-1))
# n=5
# print(fact(n))

# n=5
# m=5
# mat=[[1,2,3,4,5],
#      [6,7,8,9,10],
#      [11,12,13,14,15],
#      [16,17,18,19,20],
#      [21,22,23,24,25]]
# for i in range(m):
#     for j in range(i):
#         print(" ",end=" ")
#     print(mat[i][i])

# for i in range(n-1,-1,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     print(mat[i][j])

# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1: 
#             print(mat[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()

# e * e * e 
# * * * * *
# e * e * e
# * * * * *
# e * e * e
# for i in range(n):
#     for j in range(n):
#         if i % 2 == 0 and j % 2 == 0: 
#             print("e", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# 0 1 2 3 4
# h h h h h   
# * h h h *   1
# h h * h h   2
# * * h h *   3
# * h h * h   4

# 00  40 
# 12  
# 21 23 24

#check length of column and row
mat=[[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
m=len(mat) #lenght of row
n=len(mat[0]) #length of column
t=26
for i in range(m):
    for j in range(n):
        if mat[i][j]==t:
            print("True")
        else:
            print("False")
            break