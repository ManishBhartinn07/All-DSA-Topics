def lcp(str):
    prefix = str[0]
    for s in str[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
str=["flower","flow","flight"]
print(lcp(str))


