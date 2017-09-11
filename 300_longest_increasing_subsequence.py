#dp solution O(n^2) solution  https://www.youtube.com/watch?v=CE2b_-XfVDk
def lengthOfLIS(nums):
    
    n = len(nums)
    if n == 0:
        return 0
    dp = [1]*(n+1)
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
    
    
    
nums = [10, 9, 2, 5, 3, 7, 101, 18]
lengthOfLIS(nums)


#more clear result
#time complexitu is O(n2) : two loops of n are there
#space complexity is O(n) : array of size n is used
def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print dp
            
            
    
    
    
    
nums = [3,4,-1,0,6,2,3]
lengthOfLIS(nums)
