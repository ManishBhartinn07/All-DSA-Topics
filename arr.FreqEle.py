def max_Freq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0)+1
    c=0
    a=[]
    for val,r in freq.items():
        a.append(r)
    print(a)
    # a.sort()
    m=max(a)
    for i in range(len(a)):
        if m==a[i]:
            c+=1
            continue
    print(m*c)
    return freq
arr = [1,2,3,4,5]
print(max_Freq(arr))