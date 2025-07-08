#Having n number of childs

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]
#         self.parent=None

    
#Binary tree
#inorder traversal
#Left Root Right
# If root is NULL, then return
# Inorder (root -> left)
# Process root (For example, print root’s data)
# Inorder (root -> right)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
# def inOrder(node):
#     if node is None:
#         return
#     inOrder(node.left)
#     print(node.data,end=" ")
#     inOrder(node.right)

# # If root is NULL then return
# # Process root (For example, print root’s data)
# # Preorder (root -> left)
# # Preorder (root -> right)
# def preorder(node):
#     if node is None:
#         return
#     print(node.data,end=" ")
#     preorder(node.left)
#     preorder(node.right)

# # If root is NULL then return
# # Postorder (root -> left)
# # Postorder (root -> right)
# #  Process root (For example, print(root->data))
# def postorder(node):
#     if node is None:
#         return 
#     postorder(node.left)
#     postorder(node.right)
#     print(node.data,end=" ")
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.right=Node(6)

# inOrder(root)
# print()
# preorder(root)
# print()
# postorder(root)

#Get height of binary tree
# from collections import queue

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
# def PostOrder(node):
#     if node is None:
#         return 
#     PostOrder(node.left)
#     PostOrder(node.right)
#     print(node.data,end=" ")

# root=Node(4)
# root.left=Node(5)
# root.left.right=Node(8)
# root.left.left=Node(2)
# root.left.left.left=Node(1)
# root.left.left.right=Node(3)
# root.right=Node(15)
# root.right.left=Node(12)
# root.right.right=Node(18)
# root.right.left.left=Node(11)
# root.right.left.right=Node(13)
# root.right.right.left=Node(17)

# PostOrder(root)

#N tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
#     def add_subcategory(self, subcategory):
#         self.children.append(subcategory)
#     def display(self,lvl=0):
#         print(" " * (lvl*2) + str(self.value))
#         for child in self.children:
#             child.display(lvl + 1)
# root = Node("Electric")
# child1 = Node("Kitchen")
# child2 = Node("Beauty")
# child3 = Node("Toys")
# sub_child=child3.append("Kids")

# root = CategoryNode("Categories")

# electric = CategoryNode("Electric")
# kitchen = CategoryNode("Kitchen")
# beauty = CategoryNode("Beauty")
# toys = CategoryNode("Toys")



# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []

#     def add_c(self, child):
#         self.children.append(child)

#     def display(self, level=0):
#         print(" " * (level * 2) + self.name)  
#         for child in self.children:
#             child.display(level + 2)
#             print("->")
# root = Node("Categories")

# electric = Node("Electric")
# kitchen = Node("Kitchen")
# beauty = Node("Beauty")
# toys = Node("Toys")

# root.add_c(electric)
# root.add_c(kitchen)
# root.add_c(beauty)
# root.add_c(toys)

# kids = Node("Kids")
# adult = Node("Adult")
# sports = Node("Sports")

# toys.add_c(kids)
# toys.add_c(adult)
# toys.add_c(sports)

# plate=Node("Plate")
# kitchen.add_c(plate)
# root.display()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.parent=None
#         self.children=[]
#     def add_child(self,child):
#         child.parent=self
#         self.children.append(child)
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level+=1
#             p = p.parent
#         return level

#     def print_Tree(self):
#         spaces = " " * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_Tree()

# def product_tree():
#     root = Node("Electronics")

#     laptop = Node("Laptop")
#     laptop.add_child(Node("MacBook"))
#     laptop.add_child(Node("HP"))
#     laptop.add_child(Node("Acer"))

#     phone = Node("Phones")
#     phone.add_child(Node("Moto"))
#     phone.add_child(Node("Apple"))

#     headphn = Node("Headphn")
#     headphn.add_child(Node("Boat"))
#     headphn.add_child(Node("Apple"))
#     root.add_child(laptop)
#     root.add_child(phone)
#     root.add_child(headphn)
#     return root

# root = product_tree()
# root.print_Tree()


# class TreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.parent=None
#         self.children=[]
#     def add_child(self,child):
#         child.parent=self
#         self.children.append(child)
#     def get_lvl(self):
#         l = 0
#         p=self.parent
#         while p:
#             l+=1
#             p=p.parent
#         return l
#     def print_Tree(self):
#         spaces = " " * self.get_lvl() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_Tree()
    
# def structure():
#     root=TreeNode("Nilupul (CEO)")
#     Chinmay = TreeNode("Chinmay (CTO)")
#     Vishwa = TreeNode("Vishva (Infastructure Head)")
#     Chinmay.add_child(Vishwa)

#     Dhawal = TreeNode("Dhawal (Cloud Manager)")
#     Vishwa.add_child(Dhawal)

#     Dhawal.add_child(TreeNode("Manish (Sbka Baap)"))

#     Vishwa.add_child(TreeNode("Abhijit (App Manager)"))

#     Aamir = TreeNode("Aamir (Application Head)")
#     Chinmay.add_child(Aamir)
#     Gels = TreeNode("Gels (HR Head)")
#     Gels.add_child(TreeNode("Peter (Recruitment Manager)"))
#     Gels.add_child(TreeNode("Waqas (Policy Manager)"))

#     root.add_child(Chinmay)
#     root.add_child(Gels)

#     return root

# root=structure()
# root.print_Tree()

#BST
# class BSTNode:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def add_child(self,data):
#         if data == self.data: #Value already exists
#             return 
        
#         if data < self.data:
#             if self.left: #Left have some value ,Not a leaf node
#                 self.left.add_child(data)
#             else:
#                 self.left=BSTNode(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.left=BSTNode(data)
#     def inorder(self,data):
#         if self.left:
#             return 

'''
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        
        return node
    def inOrder(self,root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

tree=Tree()
root = tree.createNode(5)
# print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

tree.inOrder(root)
'''

#Taking user input

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left=self.insert(node.left, data)
        else:
            node.right=self.insert(node.right ,data)
        return node
    
    def inOrder(self,root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data,end=" ")
            self.inOrder(root.right)
    def preOrder(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    def postOrder(self,root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end = " ")
    
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left), self.height(root.right))+1
    
    def lot(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            root = q.pop(0)
            print(root.data,end=" ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
        return root
             

tree = Tree()
vals = list(map(int, input().split()))

root = tree.createNode(vals[0])
for val in vals[1:]:
    tree.insert(root, val)
print("Inorder")
tree.inOrder(root)
print("\nPreorder")
tree.preOrder(root)
print("\nPostorder")
tree.postOrder(root)
print("\nheight", tree.height(root))

print("\nLOT")
tree.lot(root)