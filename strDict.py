# a={1:"first" , 2:"second" , 3:"third"}
# print(a[1])

# # print(a[4]) #give error
# #but what if we use some condition 
# print(a.get(4,"Not found"))

# print(a.get(2,"Not found"))

'''How to merge the keys and values'''
#dict = {key1:value1,key2:value2,.....}
'''
keys = [1,2,3]
values = ["first","second","third"]
d = dict(zip(keys,values)) #zip merges two lists
print(d)

#add values
d[4]="fourth"
print(d)

#delete
del d[3]
print(d)

d[3] = ["third","added"]
print(d)
'''

'''User Input'''

# n=int(input("Enter number of key-value pairs: "))
# d = {}
# for i in range(n):
#     key = input()
#     value = input()
#     d[key] = value

# print(d)

'''Default dictionary'''
#provides default values to key that does not exixts, preventing key error
'''
from collections import defaultdict
# d={1:'one',2:'two'}
d=defaultdict(str,{1:'one',2:'two'})
print(d["unknown"]) #now its not giving any error
'''

#but if want to print anything else, koi condition so we use lambda
from collections import defaultdict
d = defaultdict(lambda: "Not found", {1:'one',2:'two'}) 
print(d['abc'])