#dp Solution TLE
def numSquares(n):
    dp = [0]+n*[n]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i < j*j:
                break
            else:
                dp[i] = min(dp[i],dp[i-j*j] + 1)
                
    return dp[n]
    

t = 37
print numSquares(t)



#bfs 
def numSquares(n):
    mem, stk, level = {n},{n},0
        
    while stk:
        if 0 in mem:
            return level
        stk = {(i-j*j) for i in stk for j in range(1,int(i**0.5)+1) if i>=j*j}
        mem.update(stk)
        level +=1
    return -1
    
print numSquares(100)


#dp Solution Accept 
def numSquares(n):
    dp = [0]+n*[n]
    for i in range(1,n+1):
        for j in range(1,int(i**0.5)+1):
            if i < j*j:
                break
            else:
                dp[i] = min(dp[i],dp[i-j*j] + 1)
                
    return dp[n]
