#Used for efficient searching, deletion, insertion
#generates fixed output, using mathematical formulas
#hash set = set()
#check array is subset of another array
#O(m+n) --- m and n is size of arrays
# arr1=[1,2,3,4,5]
# arr2=[3,6]

# def h(a,b):
#     hash_set = set(a)
#     for num in b: #check each element is present in hash set
#         if num not in hash_set:
#             return False
#     return True

# c=h(arr1,arr2)
# print(c)

#Get intersection and union of two linked list
#O(m+n)
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def print_list(head):
#     c=head
#     while c:
#         print(c.data,end=" ")
#         c=c.next
#     print()

# def get_intr(head1,head2):
#     seen=set()
#     result=None

#     p=head1
#     while p:
#         seen.add(p.data)
#         p=p.next
    
#     p=head2
#     while p:
#         if p.data in seen:
#             new_node=Node(p.data)
#             new_node.next=result
#             result=new_node
#         p=p.next
#     return result
# def printUI(head1,head2):
#     intr_list = get_intr(head1,head2)
#     print("Intersection list: ")
#     print_list(intr_list)
# p1=Node(1)
# p1.next=Node(2)
# p1.next.next=Node(3)
# p1.next.next.next=Node(4)

# p2=Node(1)
# p2.next=Node(4)
# printUI(p1,p2)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def print_list(head):
#     c=head
#     while c:
#         print(c.data,end=" ")
#         c=c.next
#     print()

# def get_intr(head1,head2):
#     seen1=set()
#     result=None

#     p=head1
#     while p:
#         seen1.add(p.data)
#         p=p.next
#     p=head2
#     while p:
#         if p.data in seen1:
#             new_node=Node(p.data)
#             new_node.next=result
#             result=new_node
#         p=p.next
#     return result

# def get_Union(head1,head2):
#     seen=set()
#     result=None

#     p=head1
#     while p:
#         seen.add(p.data)
#         p=p.next
#     p=head2
#     while p:
#         seen.add(p.data)
#         p=p.next
    
#     tail=None
#     #Insert all unique elements
#     for i in seen:
#         new_node = Node(i)
#         if result is None:
#             result=new_node
#             tail=new_node
#         else:
#             tail.next=new_node
#             tail=tail.next
#     return result


# def printUI(head1,head2):
#     intr_list = get_intr(head1,head2)
#     union_list = get_Union(head1,head2)
#     print("Union")
#     print_list(union_list)
#     print_list(intr_list)

# head1 = Node(1)
# head1.next = Node(2)
# head1.next.next = Node(3)
# head1.next.next.next = Node(4)
# head2 = Node(1)
# head2.next = Node(4)
# head2.next.next = Node(3)
# printUI(head1,head2)


#two Sum-pair with given sum
# arr=[1,-3,4,2,-2]
# t=0
# def pair_sum(arr,t):
#     s=set()

#     for num in arr:
#         c=t-num
#         if c in s:
#             return True
#         s.add(num) 
#     return False
# if pair_sum(arr,t):
#     print("T")
# else:
#     print("F")

# Find Itinerary from a given list of tickets
# d = {
#     "Chennai": "Banglore",
#     "Bombay": "Delhi",
#     "Goa": "Chennai",
#     "Delhi": "Goa"
# }
# Output -- Bombay -> Delhi, Delhi -> Goa, Goa -> Chennai, Chennai -> Banglore,

# class Solution():
#     def __init__(self):
#         pass
#     def rev_map(self,d):
#         rev_d=dict()
#         # Reverse mapping
#         for i in d:
#             rev_d[d[i]]=i
#         # get starting point
#         for i in rev_d:
#             if rev_d[i] not in rev_d:
#                 strpt=rev_d[i]
#                 break
#         while(strpt in d):
#             print(strpt,"->",d[strpt])
#             strpt=d[strpt]


# d=dict()
# d["Chennai"] = "Banglore"
# d["Bombay"] = "Delhi"
# d["Goa"] = "Chennai"
# d["Delhi"] = "Goa"
# obj=Solution()
# obj.rev_map(d)

# Find four elements a, b, c and d in an array such that a+b = c+d

# def find_sum(arr: list, n: int):
#     map={}
#     sum=0
#     for i in range(n):
#         for j in range(i+1,n):
#             sum+=arr[i]+arr[j]
#             if sum in map:
#                 print(f"{map[sum]} and ({arr[i],arr[j]})")
#                 return
#             else:
#                 map[sum]=[arr[i],arr[j]]
# arr = [3, 4, 7, 1, 2, 9, 8]
# n = len(arr)
# find_sum(arr, n)

# Longest Subarray with 0 Sum
# def z_sum(arr):
#     n=len(arr)
#     max_len = 0

#     for i in range(n):
#         sum=0
#         for j in range(i,n):
#             sum+=arr[j]
#             if sum==0:
#                 max_len=max(max_len,j-i+1)
#     return max_len

# a=[1,2,3,-8,4,1]
# print(z_sum(a))

# def z_sum(arr):
#     presum={}
#     n=len(arr)
#     max_len=0

#     sum=0
#     for i in range(n):
#         sum+=arr[i]
#         if sum==0:
#             max_len=i+1
#         if sum in presum:
#             max_len=max(max_len,i-presum[sum])
#         else:
#             presum[sum]=i
#     return max_len
# print(z_sum([15, -2, 2, -8, 1, 7, 10, 23]))

# def min_sum(arr,t):
#     n=len(arr)
#     r=float('inf')

#     for i in range(n):
#         c=0
#         for j in range(i,n):
#             c+=arr[j]
#             if c==t:
#                 r=min(r,j-i+1)
#                 break
#     if r == float('inf'):
#         return 0
#     return r

def min_arr(arr,t):
    n=len(arr)
    l=0
    c_sum=0
    min_len=float('inf')
    for r in range(n):
        c_sum+=arr[r]

        while c_sum>=t:
            min_len=min(min_len,r-l+1)
            c_sum-=arr[l]
            l+=1
    return 0 if min_len==float('inf') else min_len

arr=[1,2,3,4,5]
t=7
print(min_arr(arr,t))




















