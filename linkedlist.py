# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def traverse(head,s):
#     current = head
#     s=0
#     while current is not None:
#         print(current.data,"->")
#         s += current.data 
#         current = current.next
#     print("None")
#     print("sum= ",s)

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# head = node1
# s=0
# traverse(head,s)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def trv(head,b):
#     curr = head
#     b = 0
#     p = 2
#     i = 0
#     while curr is not None:
#         if curr.data == 1:
#             b += p**i
#             print(p**i)
#         i += 1
#         curr = curr.next 
#     return b

class Node:
    def __init__(self,val):
        self.val=val
        self.next=next
def dup(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else: current = current.next
    kreturn head
            
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node1.next = node2
node2.next = node3
head = node1

# b=0
# print(trv(head,b))