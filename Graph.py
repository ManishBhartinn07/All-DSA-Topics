#Directed 
# def add_edge(mat,i,j):
#     mat[i][j]=1
#     mat[j][i]=1
# def display(mat):
#     for row in mat:
#         print(' '.join(map(str,row)))
# v=4
# mat = [[0] * v for _ in range(v)]
# print(mat)
# add_edge(mat, 0, 1)
# add_edge(mat, 0, 2)
# add_edge(mat, 1, 2)
# add_edge(mat, 2, 3)
# print("Adjacency Matrix:")
# display(mat)

'''
def add_edge(mat,i,j):
    mat[i][j]=1
    mat[j][i]=1
def display(mat):
    for row in mat:
        print(' '.join(map(str, mat)))
v=int(input())
e=int(input())
mat = [[0] * v for _ in range(e)]
for _ in range(e):
    u, v = map(int, input().split())
    add_edge(mat,u,v)
display(mat)'
'''

#Undirected
def add_edge(mat,i,j):
    mat[i].append(j)
    mat[j].append(i)
def display(mat):
    for i in range(len(mat)):

        for j in mat[i]:
            print(j,end=" ")
        print()

v=4
mat = [[] for _ in range(v)]
add_edge(mat,0,1)
add_edge(mat,0,2)
add_edge(mat,1,2)
add_edge(mat,2,3)
display(mat)