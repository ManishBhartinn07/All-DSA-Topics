#Level Order Traversal (Breadth First Search or BFS) of Binary Tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    @staticmethod
    def levelOrec(root,level,res):
        if root is None:
            return
        
        if len(res) <= level: #1 0 2 1  If needed
            res.append([])
        res[level].append(root.data)
        Node.levelOrec(root.left,level+1,res) # type: ignore
        Node.levelOrec(root.right,level+1,res)
    @staticmethod 
    def BFS(root):                                                                                               
        res=[]
        Node.levelOrec(root,0,res)
        return res
root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.right = Node(4)
root.right.right.left = Node(6)
root.right.right.right = Node(5)
res = Node.BFS(root)

    # Print the result
for level in res:
    for data in level:
        print(data, end=" ")

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def Sol(self,root,k):
        if root is None:
            return []
        stk=[(root,0)] #root, level
        result = []
        while stk:
            curr, level = stk.pop()
            if curr is None:
                continue
            if level==k:
                result.append(curr.data)
            stk.append((curr.left,level+1))
            stk.append((curr.right,level+1))
        return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(8)

k = 2
result = root.Sol(root, k)
print(" ".join(map(str, result)))

#    1
#  2   3
# 4  5  8

#Sho