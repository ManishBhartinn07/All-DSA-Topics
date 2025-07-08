# n=9
# print(bin(n)) #Print in binary
# b=bin(n)[2:]
# # b.reversed()
# r=b[::-1]
# rev = int(r,2)
# print(rev)

# a=[1,2,3]
# b=0
# for ele in a:
#     b=(b*10)+ele
# b=b+1

# print(b)

# a="11"
# b="1"
# # print(bin(a+b)[2:])
# c=int(a,2)
# d=int(b,2)
# e=c+d
# print(bin(e)[2:])

# n=11
# a=bin(n)[2:]
# a=str(a)
# c=0
# # for i in range(len(a)):
# #     if a[i]=="1":
# #         c+=1
# c=a.count("1")
# print(c)

# x=1221
# r=str(x)
# rev=r[::-1]
# print(rev)
# print(int(r[::-1]) == x)

# a="AA"
# # print(ord(a)-64)
# s=list(a)
# print(s)
# sum=0
# if len(s)==1:
#     print(ord(a))

# for i in range(len(s)-1):

#     c=ord(s[i])-64
#     d=26-s[i+1]
#     sum += c + 

# print(sum)

a="kvbd"
# l=["k","v","b","d"]
l=list(a)
l.sort()
print(l)