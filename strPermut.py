# a="ABC"
# b=" ".join(a)
# print(b)

def p(index,s,ans):
    if index == len(s):
        # ans.append("".join(s))
        ans.append("".join(s))
        return
    seen = set()
    for i in range(index,len(s)):
        if s[i] in seen:
            continue
        seen.add(s[i])
        s[index],s[i] = s[i],s[index]
        p(index+1,s,ans)
        s[index],s[i] = s[i],s[index]
def permt(s):
    ans = []
    p(0,list(s),ans)
    # return sorted(set(ans))
    return sorted(ans)
str = "112"
res = permt(str)

# sorted(set(res))

print(res,end=" ")