def LCS(text1,text2):
    dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)] #Make 2D matrix in which put 0 on all positions
    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1): #Start from last and last value goes as bottom up so we return dp[0][0]
            if text2[j] == text1[i]:
                dp[i][j]= 1+dp[i+1][j+1] #if they matches we add +1 diagonally to up
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                #if they do not match then we just pass the value from last down diagonals to the up 
    return dp[0][0]

a="ABCD"
b="BD"
print(LCS(a,b))

