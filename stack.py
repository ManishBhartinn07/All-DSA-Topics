# Last In, First Out.
# Push,
# Pop(Upr waale ele ko remove krna or wapis laana),
# Peek(stack ki upr waali element ko dekhna , remove nhi krta) print head data
# Check if empty

# Use list []

# stack = []

# # Push (add element) --- append
# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)

# # Pop (upr waali item ko hatao or wapis laao)
# top_item = stack.pop()
# print(top_item)
# print(stack)

# # Peek (Top item ko dekhna)
# top_item = stack[-1]
# print(top_item)

# # Check empty stack
# is_empty = len(stack)==0
# print(is_empty)

# n=int(input())
# stack = []
# for _ in range(n):
#     data=input()
#     stack.append(data)

# print(stack)
# i=int(input())
# def removefromEnd(stack,n,i):
#     r = n - i 
#     if n!=0:
#         stack.pop(r)
#         return stack
#     else:
#         return []

# removefromEnd(stack,n,i)
# print(stack)

#Valid Paranthesis
# def isValid(s: str) -> bool:
#         stack = []
#         pairs = {')': '(', ']': '[', '}': '{'}
#         for c in s:
#             if c in "([{":
#                 stack.append(c)
#             else:
#                 if not stack or stack[-1] != pairs[c]:
#                     return False
#                 stack.pop()
#         return not stack
# s="[{}]("
# print(isValid(s))


# def isValid(s):
#     stack=[]
#     pairs = {')':'(', ']':'[','{':'}'}
#     for c in s:
#         if c in "([{":
#             stack.append(c)
#         else:
#             if not stack or stack[-1] != pairs[c]:
#                 return False
#             stack.pop()
#         return not stack

# st=["MinStack","push","push","push","getMin","pop","top","getMin"]

class MinStack(object):

    def __init__(self):
        self.arr=[]
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        if not self.minStack or self.minStack[-1] >=val:
            self.minStack.append(val)
    def pop(self):
        """
        :rtype: None
        """
        if self.arr[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# Instantiate MinStack object
obj = MinStack()

# Perform operations
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # Should return -3

obj.pop()
print(obj.top())     # Should return 0
print(obj.getMin())  # Should return -2




