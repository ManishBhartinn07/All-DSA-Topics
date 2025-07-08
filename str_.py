# a="hthth"
# b=a[::-1]

# c="hello"
# d="".join(reversed(c))
# print(b)
# print(c)
# def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s=s.lower()
#         s=''.join(char for char in s if char.isalnum())
#         return s==s[::-1]

# def similar(s,t):
#     i,j=0,0
#     while i<len(s) and j<len(t):
#         if s[i]==t[j]:
#             i=i+1    #if matches then take next word
#         j+=1         #if not then take next word from full string
#     return i==len(s)

# s="abc"
# t="ahbftc"

#Counter
#Check we can make string with another string

# from collections import Counter

# def st(s1,s2):
#     st1=Counter(s1)
#     st2=Counter(s2)
#     if st1&st2 == st1:
#         return True
#     return False
# s1="aba"
# s2="aab"
# print(st(s1,s2))

# str1="egg"
# str2="add"
# # print(str1.index('e')) 
# def isom(s,t):
#     map1=[]
#     map2=[]
#     for i in s:
#         map1.append(s.index(i))
#     for i in t:
#         map2.append(t.index(i))
#     if map1==map2:
#         return True
#     return False
# print(isom(str1,str2))

#abba
#dog cat cat dog
# str1="abba"
# str2="dog cat cat dog"
# str2 = str2.split()  #['dog', 'cat', 'cat', 'dog']
# str1=set(str1)
# print(str1)
# #zip --> pair strings or set, tuples 
# print(list(zip(str1,str2))) #[('a', 'dog'), ('b', 'cat')]

# s1="abba"
# s2="dog cat cat dog"
# def ppair(s1,s2):
#     s2=s2.split()
#     return len(s1)==len(s2) and len(set(s1)) == len(set(s2)) == len(set(zip(s1,s2)))
# print(ppair(s1,s2))

#Anagrma
# s1="abcdefg"
# s1=sorted(s1)
# s2="acbdgfe"
# s2=sorted(s2)
# print(s2)
# if s1==s2:
#     print("Treu")
# else:
#     print("flase")
    
# l1 = set(map(int, input().split()))
# l2 = set(map(int, input().split()))
# l3 = l1.symmetric_difference(l2)
# print(l3)

#reverse the words in the sentence
# Input: s = " i like this program very much "
# Output: "much very program this like i"
# str = "Python is a coding lang"
# rev_str = str.split()  #taking every word into list ["Python","is","a"....]
# rev_str = rev_str[::-1] #To reverse
# rev_str = " ".join(rev_str) #To convert list into string
# print(rev_str)


# print(chr(65))
# print(ord('a'))

# a="Hello world !"
# # b=a.strip().split()  #Strip removes the extra chars and symbols
# # c=len(b)-1
# # print(len(b[c]))
# reversed(a)
# print(a)


# Reversed string 
# s = ["h","e","l","l","o"]
# l,r=0, len(s)-1
# while l<r:
#     s[l],s[r]=s[r],s[l]
#     l+=1
#     r-=1
# print(s)


# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# s = "barfoothefoobarman"
# words = ["foo","bar"]
# c=0
# n=len(words[0])
# for i in range(len(s)):
#     for char in words:
#         if char in s:
#             c+=1
#             i+=3
#         else:
#             s=s.replace(s[i],"0")
# print(s)

# s=s.replace("b","")
# print(s)


# a="Hello"
# a=a.lower()
# l=list(a)
# l.sort()
# l=set(l)
# print(l)
# a1="qwertyuiop"


# a2="asdfghjkl"
# a3="zxcvbnm"


arr=[1,0,2,4,1,3]
arr.sort()

print(arr)

if arr[0]==0:
    arr[0],arr[1] = arr[1],arr[0]
print(arr)

arr="".join(str(i) for i in arr)
print(arr)
