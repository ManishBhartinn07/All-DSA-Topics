def convertToTitle(c):
    res=""
    while c>0:
        c-=1
        char=chr(c%26 + ord('A'))
        res = char+res()