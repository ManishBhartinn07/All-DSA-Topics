# n=input("Enter number : ")
# rev=0
# while n>0:
#     rev = rev * 10 + (n%10)
#     n//=10
# print(rev)

#reverse a string
# str="abcd"
# rev=""
# for char in str:
#     rev = char + rev
# print(rev)

n=123
r=0
while n>0:
    r=r*10 + n%10
    n//=10
print(r)