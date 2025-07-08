# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left=None
#         self.right=None
#     def height(root):
#         if root is None:
#             return -1
#         lh=Node.height(root.left)
#         rh=Node.height(root.right)
#         return max(lh,rh) + 1
# root=Node(12)
# root.left = Node(8)
# root.right = Node(18)
# root.left.left = Node(5)
# root.left.right = Node(11)
# print(Node.height(root))

#Diameter of binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def dia(root,res):
        if root is None:
            return -1
        lh=Node.dia(root.left,res)
        rh=Node.dia(root.right,res)
# Check if diameter of root is greater
# than res

        res[0] = max(res[0], lh+rh)
        return max(rh,lh)+1
    def diameter(root):
        res=[0]
        Node.dia(root,res)
        return res[0]
root = Node(5)
root.left = Node(8)
root.right = Node(6)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(9)
root.left.left.left = Node(3)
root.left.right.left = Node(7)
root.right.left.right = Node(9)
print(Node.diameter(root))

