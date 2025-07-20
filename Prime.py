# import math
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%1==0:
#             return False
#     return True

# n=2
# print(is_prime(n))

'''
import math
def p(n):
    s=str(n)
    # even positions are 0,2,4
    ep=False
    pn=False
    for i in range(len(s)):
        if s[i]==0 and s[i]%2==0:
            ep=True
#Check prime at odd
    if int(s)<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if s[i]%2!=0:
            if s[i]%1==0:
                pn=True
    return ep and pn
n=3245
print(p(n))
'''
