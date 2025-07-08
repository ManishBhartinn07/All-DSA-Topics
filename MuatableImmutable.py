# Tuple 
#immutable
# a=(1,2,3)
# a[0]=2
# print(a)

#set
#mutable
# a={1,2,3}
# a.add(4)
# print(a)

# Check if mutable or immutable
# x=(1,2,3)
# try:
#     x[0]=9
# except TypeError:
#     print("Immutable!")

# a={1,3,2}
# print(a)
# n=[8,4,4]
# if n[0]==n[1] or n[1]==n[2] or n[2]==n[0]:
#     print("yes")
# else:
#     print("no")

# a=12
# for i in range(1,21):
#     print(f"{a} * {i} = {a*i}")

# l=["Harry","Sohan","Ram","Sahil"]
# for i in range(len(l)):
#     if l[i].startswith("S"):
#         print(f"Greets for {l[i]}")

a=[0,0,0,1]
m=max(a)
for i in range(len(a)):
    if 2*a[i]>m:
        t=-1
    else:
        t=1
print(t)
