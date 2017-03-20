class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        n = len(nums)/ 2
        nums = dict(Counter(nums))
        for key in nums:
            if nums[key] > n:
                return key


def majorityElement(nums):
    
    return sorted(nums)[len(nums)/2]
