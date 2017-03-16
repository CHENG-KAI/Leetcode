def maxSubArray(nums):
    for i in xrange(1,len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], nums[i])
    return max(nums)


    
nums = [10,1,1,40,-20,10]
print maxSubArray(nums)
