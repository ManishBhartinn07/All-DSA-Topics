# class Node:
#     def __init__(self,data):
#         self.data=data #Ye node data ko rakhta hai
#         self.next=None #Next node khali rakho

# class LL:
#     def __init__(self):
#         self.head = None #initl the ll
    
#     def append(self, data): #Nya node add kro ll me
#         #Make new Node
#         nya_Node = Node(data)

#         #Check empty llist
#         if not self.head: #Node null hai?
#             self.head = nya_Node #Nye node me daal do
#             return
        
#         current = self.head #Start from head
#         while current.next:
#             current = current.next #Jb tk end Node na aa jaaye
#         current.next = nya_Node # nya node link ho rha last me

#     def printll(self):
#         current = self.head
#         while current:
#             print(current.data, end="->")
#             current = current.next
#         print("None")

# l1=LL()
# # l1.append(1)
# # l1.append(2)
# # l1.append(3)

# n=int(input())
# for _ in range(n):
#     data = input()
#     l1.append(data)

# l1.printll()


# class Node:
#     def __init__(self,data):
#         self.data=data #self ke andr data and next jayenge
#         self.next=None

# class LL:
#     def __init__(self):
#         self.head=None
#     def append(self,data):
#         new_Node=Node(data)
#         if not self.head:
#             self.head=new_Node
#             return
        
#         current = self.head
#         while current.next:
#             current=current.next
#         current.next=new_Node

#     def printL(self):
#         current = self.head
#         count=0
#         while current:
#             print(current.data," ")
#             current=current.next
#             count+=1
#         print("Total len: ",count)

# l1=LL()
# l1.append(1)
# l1.append(2)
# l1.append(3)
# l1.printL()

