#sum of factorial of number is equals to the original number
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1) 
def c(n):
    s=0
    for digit in str(n):
        s += fact((int(digit)))
    return s

n=145
if c(n)==n:
    print("Strong Number")
else:
    print("No!")
'''

import math
def c(n):
    on=n
    count=0
    while n>0:
        d=n%10
        count+=math.factorial(d)
        n//=10
    return on==count
print(c(145))

