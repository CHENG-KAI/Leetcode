def rod(nums):
    x = 0
    y = 0
    for i in xrange(len(nums)):
        if (1&i):
            x = max(x+nums[i],y)      
        else:
            y = max(y+nums[i],x)
    return max(x,y)
    
nums = [1,10,5,3,7]
print rod(nums)



def rob(nums):
    n = len(nums)
    dp = [0] *(n+1)
    if n > 0:
        dp[1] = nums[0]
    for i in range(2,n+1):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
    return dp[n]
    
nums = [1,10,5,3,7]
print rob(nums)



def rob(nums):
        
    last, now = 0, 0
        
    for i in nums: 
        last, now = now, max(last + i, now)
                
    return now
    
nums = [2,1,1,2]
print rob(nums)
