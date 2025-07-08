'''There are N passengers who have shown interest in buying the gold. The i(th) passenger
 agrees to buy a[i] grams of gold by paying v[i] dollars. Dawson wants to escape from the 
 police and also maximize the profit. Can you help him maximize the profit?

Note: The i(th) passenger would buy exactly a[i] grams if the transaction is successful.

Input Explanation:
The first line contains two space separated integers, N and X, where N is the number of 
passengers who agreed to buy and is the stolen amount of gold (in grams).
N lines follow. Each line contains two space separated integers - v[i] and a[i], 
where is the the value which the i(th) passenger has agreed to pay in exchange for a[i] grams of gold.

Output Explanation:
If it's possible for Dorsey to escape, print the maximum profit he can enjoy, otherwise print Got caught!.

Constraints:
1<= X <=5000
1<=N<=10^6
all v[i]'s and a[i]'s are less than or equal to 10^6 and greater than 0 
Example 1:
Input
4 10
460 4
590 6
550 5
590 5

Output
1140
'''

# def maxProfit(n,x,v,a):
#     from collections import defaultdict
#     dict=defaultdict(int)
#     dict[0]=0
#     for i in range(n):
#         vi, ai = v[i], a[i]
#         new_dict = dict.copy()
#         for w,val in dict.items():
#             if w+ai <= x:
#                 new_dict[w+ai] = max(new_dict[w+ai], val + vi)
#         dict = new_dict
#     max_profit = max(dict.values())
#     return max_profit if max_profit > 0 else "Failed"

# n,x = map(int, input().split())
# v,a = [],[]
# for _ in range(n):
#     vi,ai = map(int,input().split())
#     v.append(vi)
#     a.append(ai)
# r=maxProfit(n,x,v,a)
# print(r)


#optimised approach

def max_value(N, X, v, a):
    dp = [0] * (X + 1) 
    for i in range(N):
        vi, ai = v[i], a[i]
        for w in range(X, ai - 1, -1):
            dp[w] = max(dp[w], dp[w - ai] + vi)
    max_profit = max(dp)
    return max_profit if max_profit > 0 else "Got caught!"

N, X = map(int, input().split())
v = []
a = []
for _ in range(N):
    vi, ai = map(int, input().split())
    v.append(vi)
    a.append(ai)
result = max_value(N, X, v, a)
print(result)



