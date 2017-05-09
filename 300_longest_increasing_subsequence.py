#dp solution O(n^2) solution
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



