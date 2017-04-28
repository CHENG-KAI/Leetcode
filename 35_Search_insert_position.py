def mySqrt(target,nums):
    return bisect.bisect_left(nums,target)
    
    

nums = [1,3,5,7]
target = 3
import bisect
print mySqrt(target,nums)
