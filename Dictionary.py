import math
a="abcabcab"
o=[]
e=[]
for i in range(len(a)):
    if a.count(a[i]) %2!=0:
        o.append(a.count(a[i]))
    else:
        e.append(a.count(a[i]))

print(max(o)-max(e))