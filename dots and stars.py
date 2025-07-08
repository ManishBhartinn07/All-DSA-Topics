
# import math

# for y in range(12, -12, -1):
#     for x in range(-30, 30): 
#         formula = ((x * 0.04)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.04)**2 * (y * 0.1)**3
#         if formula <= 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  


'''
*
**
***
****
'''
'''a=4
for i in range(1,a+1):
    print("*"*i)
'''


'''
  *
 ***
*****
'''
n=4
for i in range(1,n+1):
    print(" "* (n-i),end=" ")
    print("*"* (2*i-1),end=" ")
    print("")