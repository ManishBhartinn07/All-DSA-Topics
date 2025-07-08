str="ZY"
str=list(str)
print(str)
# print(ord(str)-64)
s=0
for i in range(len(str)):
    s=s+(ord(str[i])-64)
print(s)